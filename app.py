import os
import json
from flask import Flask, render_template, request, jsonify
from data.agri_data import (
    SCHEMES_DATABASE, 
    MANDI_PRICE_DATA, 
    IMPORTANT_WEBSITES, 
    LOCATIONS_DATABASE, 
    DISEASE_DATABASE
)
from crop_diagnosis import analyze_crop_image
from weather_service import get_weather_forecast
from hal_ai import hal_chat_response
from supabase_client import (
    save_crop_diagnosis, 
    save_chat_message, 
    fetch_mandi_rates_from_db, 
    is_supabase_configured
)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max image upload

@app.route('/')
def index():
    mandi_records = fetch_mandi_rates_from_db() or MANDI_PRICE_DATA
    return render_template('index.html', 
                           locations=list(LOCATIONS_DATABASE.keys()),
                           schemes=SCHEMES_DATABASE,
                           websites=IMPORTANT_WEBSITES,
                           initial_mandi=mandi_records,
                           supabase_connected=is_supabase_configured())

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "app": "KISAN AI", "supabase_connected": is_supabase_configured()})

# API: Crop Disease Diagnosis via Image Upload
@app.route('/api/diagnose', methods=['POST'])
def diagnose_crop():
    if 'image' not in request.files:
        return jsonify({"success": False, "error": "No image file provided in request"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"success": False, "error": "Empty filename selected"}), 400
    
    crop_type = request.form.get('crop_type', 'auto')
    try:
        image_bytes = file.read()
        result = analyze_crop_image(image_bytes, filename=file.filename, suspected_crop=crop_type)
        if result.get("success"):
            # Persist diagnosis event to Supabase
            save_crop_diagnosis(result, filename=file.filename)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# API: Mandi Prices with Filters
@app.route('/api/mandi-rates', methods=['GET'])
def get_mandi_rates():
    commodity = request.args.get('commodity', '').strip().lower()
    state = request.args.get('state', '').strip().lower()
    query = request.args.get('q', '').strip().lower()

    # Query Supabase table first, fallback to static dataset
    db_data = fetch_mandi_rates_from_db()
    source_data = db_data if db_data else MANDI_PRICE_DATA

    filtered = source_data
    if commodity:
        filtered = [item for item in filtered if commodity in item['commodity'].lower()]
    if state:
        filtered = [item for item in filtered if state in item['state'].lower()]
    if query:
        filtered = [
            item for item in filtered 
            if query in item['commodity'].lower() 
            or query in item['mandi'].lower() 
            or query in item['district'].lower()
            or query in item['variety'].lower()
        ]
    
    return jsonify({"success": True, "count": len(filtered), "data": filtered})

# API: Real-time Weather & Agromet Advisory
@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Indore')
    forecast = get_weather_forecast(city)
    return jsonify(forecast)

# API: Hal Multilingual AI Chatbot (with Friend's Bot Integration Hook)
from bot_adapter import USE_FRIEND_BOT, custom_friend_bot

@app.route('/api/chat', methods=['POST'])
def chat_hal():
    data = request.get_json() or {}
    message = data.get('message', '').strip()
    lang = data.get('lang', 'en')
    if not message:
        return jsonify({"success": False, "error": "Message cannot be empty"}), 400
    
    # Check if friend's custom code/endpoint is enabled
    if USE_FRIEND_BOT:
        custom_resp = custom_friend_bot(message, lang)
        if custom_resp.get("success"):
            save_chat_message(message, custom_resp.get("reply", ""), lang=lang, bot_source="Friend-Bot")
            return jsonify(custom_resp)

    # Standard built-in Hal AI response
    response = hal_chat_response(message, lang)
    if response.get("success"):
        save_chat_message(message, response.get("reply", ""), lang=lang, bot_source="Hal-Builtin")
    return jsonify(response)

# API: Government Schemes & Official Portals
@app.route('/api/schemes', methods=['GET'])
def get_schemes():
    category = request.args.get('category', '').strip().lower()
    if category:
        schemes = [s for s in SCHEMES_DATABASE if category in s['category'].lower()]
    else:
        schemes = SCHEMES_DATABASE
    return jsonify({"success": True, "schemes": schemes, "websites": IMPORTANT_WEBSITES})

if __name__ == '__main__':
    print("[KISAN AI] Server initializing on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
