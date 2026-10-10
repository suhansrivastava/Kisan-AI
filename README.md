# KISAN AI (किसान एआई) 🌾
### National Digital Agriculture & Farming Intelligence Platform

An enterprise-grade, clean, and comprehensive web platform engineered specifically for Indian farmers and agricultural practitioners. **KISAN AI** features disease diagnostics, real-time APMC/e-NAM mandi rates, agromet weather advisories, the multilingual AI farming chatbot **'Hal'**, and government welfare schemes.

---

## 🚀 Key Features

1. **🔬 Crop Disease Detection through Photos**
   - Upload any leaf photo from field scouting (JPEG, PNG, WEBP) or test with built-in crop samples.
   - Diagnoses diseases including **Tomato Early & Late Blight, Wheat Yellow Rust, Rice Blast, Potato Late Blight, and Cotton Leaf Curl Virus**.
   - Calculates visual tissue metrics: green foliage %, chlorosis %, necrotic lesions %, and dark blight spots.
   - Provides **ICAR-verified chemical fungicides/pesticides**, dosage rates, and **organic/biological alternatives** (Neem seed kernel extract, Trichoderma viride, Bordeaux mixture).

2. **📊 Mandi Price Rate Tracker**
   - Live wholesale commodity price tracking linked with major agricultural markets (Indore, Khanna, Karnal, Lasalgaon, Azadpur, Rajkot, etc.).
   - Displays Minimum, Maximum, and Modal wholesale rates (₹/Quintal), daily price trends (▲/▼), and official Government **Minimum Support Prices (MSP)**.
   - Real-time search and filtering by state and crop category.

3. **🌤️ Weather & Agromet Advisory**
   - Live weather metrics powered by Open-Meteo (temperature, apparent heat index, humidity, wind velocity, precipitation).
   - Specialized **Field Operation Advisories**:
     - **Spraying Feasibility Index**: Advises whether wind and rain allow safe foliar pesticide/fungicide application.
     - **Irrigation Decision Engine**: Calibrated against soil type and rainfall forecasts.
     - **Fungal Spore Risk Alerts**: Based on humidity and morning dew thresholds.
   - 7-Day agricultural forecast outlook.

4. **🤖 'Hal' (हल) Multilingual AI Chatbot**
   - Dedicated agricultural assistant named **Hal**.
   - Supports 6 regional languages: **Hindi (हिन्दी), English, Punjabi (ਪੰਜਾਬੀ), Telugu (తెలుగు), Tamil (தமிழ்), and Bengali (বাংলা)**.
   - Answers inquiries on crop diseases, current mandi rates, weather conditions, and government schemes.

5. **🏛️ Government Welfare Schemes & Official Portals**
   - Complete guides for **PM-KISAN, PMFBY (Crop Insurance), Kisan Credit Card (KCC), PMKSY (Per Drop More Crop), Soil Health Card, e-NAM, Paramparagat Krishi Vikas Yojana (PKVY), and SMAM (Machinery Subsidies)**.
   - Direct authentic links to official portals: e-NAM, Agmarknet, PM-KISAN, PMFBY, ICAR, IMD Mausam, and Kisan Suvidha.
   - Toll-free helplines including **Kisan Call Centre (1800-180-1551)**.

---

## 🛠️ Tech Stack & Architecture

- **Backend**: Python 3.14, Flask, Pillow (PIL image analysis)
- **Frontend**: Clean semantic HTML5, Modern CSS Design System (no hype/vibe-coding aesthetics; structured for high legibility and field usability), Vanilla JavaScript (ES6+)
- **APIs**: Open-Meteo Agromet Service, e-NAM / Agmarknet Market Schema, ICAR Plant Pathology Knowledge Base

---

## 🏃 Running the Project Locally

```powershell
# Navigate to the project directory
cd "C:\Users\Suhan\.gemini\antigravity\scratch\kisan-ai"

# Run the application
python app.py
```

Then open your browser at **`http://localhost:5000`** or **`http://127.0.0.1:5000`**.
