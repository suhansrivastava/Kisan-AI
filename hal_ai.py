import re
from data.agri_data import SCHEMES_DATABASE, MANDI_PRICE_DATA, DISEASE_DATABASE

# Greetings and responses across 6 major Indian languages
KB_RESPONSES = {
    "en": {
        "greeting": "Namaste! I am Hal, your AI Farming Assistant on KISAN AI. How can I help you today with crop diagnosis, mandi rates, weather advisory, or government schemes?",
        "fallback": "I understand your query regarding farming practices. In KISAN AI, you can inspect real-time mandi prices, check today's agromet weather, upload a photo for disease diagnosis, or apply for government schemes like PM-KISAN, PMFBY, and KCC.",
        "mandi_reply": "You can view current market rates across mandis in the 'Mandi Prices' section. Currently, Wheat is trading around ₹2,470–₹2,680/qtl, Basmati Rice at ₹4,150/qtl, and Red Onion at ₹2,450/qtl at Lasalgaon.",
        "pmkisan_reply": "Under PM-KISAN (Pradhan Mantri Kisan Samman Nidhi), eligible farmers receive ₹6,000 annually in 3 installments of ₹2,000 directly via DBT. You need an Aadhaar linked bank account and land records to register on pmkisan.gov.in.",
        "pmfby_reply": "PMFBY (Crop Insurance) protects you against drought, flood, and localized hail damage. Farmers pay only 2% premium for Kharif crops, 1.5% for Rabi, and 5% for horticultural crops.",
        "disease_reply": "To diagnose leaf spots, yellowing, or blight, navigate to the 'Crop Disease Detection' tab and upload or snap a photo of the affected plant leaf. I will analyze the symptoms and recommend organic and chemical treatments.",
        "weather_reply": "Check the 'Weather & Advisory' section to get live humidity, rainfall probability, and our Agromet Spray Feasibility index before applying fertilizers or pesticides.",
        "soil_reply": "Under the Soil Health Card Scheme, you can get 12 chemical parameters tested for free to calculate exact NPK and micronutrient dosage for your land."
    },
    "hi": {
        "greeting": "नमस्ते किसान भाई! मैं 'हल' (Hal) हूँ, KISAN AI का आपका डिजिटल कृषि सहायक। फसल रोग पहचान, मंडी भाव, मौसम सलाह या सरकारी योजनाओं के बारे में आप क्या जानना चाहते हैं?",
        "fallback": "मैं आपकी कृषि संबंधी बात समझ रहा हूँ। KISAN AI पर आप अपनी फसल की पत्ती की फोटो भेजकर बीमारी पहचान सकते हैं, ताज़ा मंडी भाव देख सकते हैं, मौसम अनुसार स्प्रे की सलाह ले सकते हैं या पीएम-किसान और फसल बीमा योजना की जानकारी ले सकते हैं।",
        "mandi_reply": "आप 'मंडी भाव' टैब में ताज़ा कीमतें देख सकते हैं। आज इंदौर मंडी में गेहूं ₹2,680/क्विंटल, करनाल में 1121 बासमती धान ₹4,150/क्विंटल, और लासलगांव में प्याज ₹2,450/क्विंटल के भाव बिक रहा है।",
        "pmkisan_reply": "पीएम-किसान योजना (PM-KISAN) के तहत पात्र किसान परिवारों को प्रति वर्ष ₹6,000 की आर्थिक सहायता 3 किश्तों (₹2,000 प्रत्येक) में सीधे बैंक खाते में दी जाती है। इसके लिए आधार कार्ड और खतौनी/भूलेख की आवश्यकता होती है।",
        "pmfby_reply": "प्रधानमंत्री फसल बीमा योजना (PMFBY) प्राकृतिक आपदाओं, सूखा, ओलावृष्टि और बाढ़ से सुरक्षा देती है। खरीफ के लिए 2%, रबी के लिए 1.5% और बागवानी फसलों के लिए केवल 5% प्रीमियम देना होता है।",
        "disease_reply": "फसल में पीलापन, काले धब्बे या पत्तियों का मुड़ना दिखे तो 'फसल रोग जांच' टैब पर जाएं और पत्ती की स्पष्ट फोटो अपलोड करें। मैं बीमारी की पहचान कर दवा और जैविक उपचार बताऊंगा।",
        "weather_reply": "'मौसम एवं कृषि सलाह' टैब में जाकर आप अपनी मंडी/जिले का मौसम, हवा की गति और स्प्रे करने का उपयुक्त समय देख सकते हैं।",
        "soil_reply": "मृदा स्वास्थ्य कार्ड (Soil Health Card) से आप अपनी मिट्टी की निःशुल्क जांच करवाकर यूरिया और डीएपी का संतुलित उपयोग कर सकते हैं।"
    },
    "pa": {
        "greeting": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਿਸਾਨ ਵੀਰੋ! ਮੈਂ 'ਹਲ' (Hal) ਹਾਂ, KISAN AI 'ਤੇ ਤੁਹਾਡਾ ਖੇਤੀਬਾੜੀ ਸਹਾਇਕ। ਦੱਸੋ ਜੀ, ਅੱਜ ਫ਼ਸਲ ਦੀ ਬਿਮਾਰੀ, ਮੰਡੀ ਦੇ ਭਾਅ, ਮੌਸਮ ਜਾਂ ਸਰਕਾਰੀ ਸਕੀਮਾਂ ਬਾਰੇ ਕੀ ਜਾਣਕਾਰੀ ਚਾਹੀਦੀ ਹੈ?",
        "fallback": "ਮੈਂ ਤੁਹਾਡਾ ਸਵਾਲ ਸਮਝ ਲਿਆ ਹੈ। KISAN AI 'ਤੇ ਤੁਸੀਂ ਕਣਕ, ਝੋਨੇ ਦੇ ਰੋਗਾਂ ਦੀ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ, ਮੰਡੀ ਦੇ ਰੇਟ ਦੇਖ ਸਕਦੇ ਹੋ ਅਤੇ ਖੇਤੀ ਸਕੀਮਾਂ ਬਾਰੇ ਪੂਰੀ ਜਾਣਕਾਰੀ ਲੈ ਸਕਦੇ ਹੋ।",
        "mandi_reply": "ਮੰਡੀ ਰੇਟ ਸੈਕਸ਼ਨ ਵਿੱਚ ਤੁਸੀਂ ਤਾਜ਼ਾ ਭਾਅ ਦੇਖ ਸਕਦੇ ਹੋ। ਖੰਨਾ ਮੰਡੀ ਵਿੱਚ ਕਣਕ ₹2,470/ਕੁਇੰਟਲ ਅਤੇ ਕਰਨਾਲ ਵਿੱਚ ਬਾਸਮਤੀ ₹4,150/ਕੁਇੰਟਲ ਦੇ ਨੇੜੇ ਵਿਕ ਰਹੀ ਹੈ।",
        "pmkisan_reply": "ਪੀਐਮ-ਕਿਸਾਨ ਸਕੀਮ ਅਧੀਨ ਹਰ ਸਾਲ ₹6,000 ਸਿੱਧੇ ਬੈਂਕ ਖਾਤੇ ਵਿੱਚ ਤਿੰਨ ਕਿਸ਼ਤਾਂ (₹2,000) ਵਿੱਚ ਮਿਲਦੇ ਹਨ। ਆਧਾਰ ਕਾਰਡ ਅਤੇ ਜ਼ਮੀਨ ਦੀ ਫਰਦ ਜ਼ਰੂਰੀ ਹੈ।",
        "pmfby_reply": "ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਫ਼ਸਲ ਬੀਮਾ ਯੋਜਨਾ (PMFBY) ਨਾਲ ਬੇਮੌਸਮੀ ਮੀਂਹ, ਗੜੇਮਾਰੀ ਅਤੇ ਸੋਕੇ ਤੋਂ ਫਸਲ ਦਾ ਪੂਰਾ ਬੀਮਾ ਮਿਲਦਾ ਹੈ।",
        "disease_reply": "ਜੇਕਰ ਪੱਤਿਆਂ 'ਤੇ ਪੀਲ਼ੀ ਕੁੰਗੀ (Yellow Rust) ਜਾਂ ਧੱਬੇ ਦਿਖਣ ਤਾਂ ਪੱਤੇ ਦੀ ਫੋਟੋ ਅਪਲੋਡ ਕਰੋ, ਮੈਂ ਤੁਰੰਤ ਦਵਾਈ ਅਤੇ ਰੋਕਥਾਮ ਦੱਸਾਂਗਾ।",
        "weather_reply": "ਮੌਸਮ ਵਾਲੇ ਪੰਨੇ 'ਤੇ ਹਵਾ ਦੀ ਗਤੀ ਅਤੇ ਮੀਂਹ ਦਾ ਅਨੁਮਾਨ ਦੇਖ ਕੇ ਹੀ ਸਪਰੇਅ ਅਤੇ ਖਾਦ ਪਾਉਣ ਦਾ ਫੈਸਲਾ ਕਰੋ।",
        "soil_reply": "ਮਿੱਟੀ ਪਰਖ ਕਾਰਡ ਨਾਲ ਆਪਣੀ ਜ਼ਮੀਨ ਦੇ ਤੱਤ ਚੈੱਕ ਕਰਵਾ ਕੇ ਖਾਦ ਦਾ ਸਹੀ ਇਸਤੇਮਾਲ ਕਰੋ।"
    },
    "te": {
        "greeting": "నమస్కారం రైతు సోదరులారా! నేను 'హల్' (Hal), KISAN AI డిజిటల్ వ్యవసాయ సహాయకుడిని. పంట తెగుళ్లు, మార్కెట్ ధరలు, వాతావరణం లేదా ప్రభుత్వ పథకాల గురించి మీకు ఏం సమాచారం కావాలి?",
        "fallback": "మీ ప్రశ్నను అర్థం చేసుకున్నాను. KISAN AI లో మీరు పంట ఆకుల ఫోటోలు అప్‌లోడ్ చేసి వ్యాధి నిర్ధారణ చేయవచ్చు, మార్కెట్ రేట్లు మరియు ప్రభుత్వ పథకాల వివరాలు తెలుసుకోవచ్చు.",
        "mandi_reply": "మార్కెట్ ధరల విభాగంలో మీరు తాజా రేట్లు చూడవచ్చు. వరి, పత్తి, మిరప, టమోటా ధరల వివరాలు అందుబాటులో ఉన్నాయి.",
        "pmkisan_reply": "పీఎం-కిసాన్ పథకం ద్వారా అర్హులైన రైతులకు ఏడాదికి ₹6,000 నేరుగా బ్యాంక్ ఖాతాలో జమ అవుతాయి.",
        "pmfby_reply": "పీఎం ఫసల్ బీమా యోజన (PMFBY) ద్వారా ప్రకృతి వైపరీత్యాలు, అకాల వర్షాల నుంచి పంటకు రక్షణ లభిస్తుంది.",
        "disease_reply": "పంట తెగుళ్ల గుర్తింపు కోసం ఆకు స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి. నేను నివారణ మందులు సూచిస్తాను.",
        "weather_reply": "మందుల పిచికారీ చేయడానికి ముందు వాతావరణం మరియు గాలి వేగం సమాచారాన్ని పరిశీలించండి.",
        "soil_reply": "సాయిల్ హెల్త్ కార్డు ద్వారా మట్టి పరీక్ష చేయించి తగినంత ఎరువులు మాత్రమే వేయండి."
    },
    "ta": {
        "greeting": "வணக்கம் விவசாய தோழரே! நான் 'ஹல்' (Hal), KISAN AI-ன் வேளாண்மை உதவியாளர். பயிர் நோய் கண்டறிதல், மண்டி விலை, வானிலை அல்லது அரசு திட்டங்கள் குறித்து உங்களுக்கு என்ன தகவல் வேண்டும்?",
        "fallback": "உங்கள் கேள்வியை புரிந்துகொண்டேன். KISAN AI மூலம் பயிர் இலைகளின் புகைப்படம் பதிவேற்றி நோய்களைக் கண்டறியலாம் மற்றும் சந்தை விலைகளை அறியலாம்.",
        "mandi_reply": "மண்டி விலை பிரிவில் தக்காளி, நெல், பருத்தி மற்றும் காய்கறிகளின் தினசரி விலைகளை நேரலையாகக் காணலாம்.",
        "pmkisan_reply": "பிஎம்-கிசான் திட்டத்தில் ஆண்டுக்கு ₹6,000 மூன்று தவணைகளில் விவசாயிகளின் வங்கிக் கணக்கில் நேரடியாக வழங்கப்படுகிறது.",
        "pmfby_reply": "பிரதம மந்திரி பயிர் காப்பீட்டுத் திட்டம் (PMFBY) மூலம் இயற்கை சீற்றங்களால் ஏற்படும் இழப்புகளுக்கு இழப்பீடு பெறலாம்.",
        "disease_reply": "பயிரில் பூச்சி அல்லது இலைப்புள்ளி நோய் இருந்தால் புகைப்படத்தை பதிவேற்றி உடனடி தீர்வு பெறுங்கள்.",
        "weather_reply": "மருந்து தெளிப்பதற்கு முன் வானிலை மற்றும் மழை முன்னறிவிப்பை கவனித்து செயல்படவும்.",
        "soil_reply": "மண் வள அட்டை மூலம் உங்கள் நிலத்தின் ஊட்டச்சத்துக்களை அறிந்து உரமிடுங்கள்."
    },
    "bn": {
        "greeting": "নমস্কার কৃষক ভাই! আমি 'হল' (Hal), KISAN AI-এর ডিজিটাল কৃষি পরামর্শক। ফসলের রোগ নির্ণয়, মান্ডি দর, আবহাওয়া বা সরকারি প্রকল্প সম্পর্কে আপনি কী জানতে চান?",
        "fallback": "আমি আপনার প্রশ্নের গুরুত্ব বুঝতে পেরেছি। KISAN AI পোর্টালে আপনি পাতার ছবি আপলোড করে রোগ নির্ণয় করতে পারেন এবং আজকের তাজা মান্ডি দর দেখতে পারেন।",
        "mandi_reply": "মান্ডি দর বিভাগে আপনি বিভিন্ন ফসলের বর্তমান বাজার দর দেখতে পারেন। ধান, গম, আলু এবং পেঁয়াজের দর নিয়মিত আপডেট হয়।",
        "pmkisan_reply": "পিএম-কিসান যোজনায় যোগ্য কৃষকরা বছরে ₹৬,০০০ টাকা তিন কিস্তিতে সরাসরি ব্যাংক অ্যাকাউন্টে পান।",
        "pmfby_reply": "প্রধানমন্ত্রী ফসল বিমা যোজনা (PMFBY) অনাবৃষ্টি ও প্রাকৃতিক দুর্যোগে ফসলের ক্ষতির সম্পূর্ণ আর্থিক সুরক্ষা প্রদান করে।",
        "disease_reply": "ফসলের কোনো পাতায় দাগ বা ব্লাইট রোগ দেখা দিলে ছবি তুলে আপলোড করুন, আমি সঠিক ওষুধ ও প্রতিকার জানাব।",
        "weather_reply": "কীটনাশক স্প্রে করার আগে বাতাসের গতিবেগ ও বৃষ্টির সম্ভাবনা আবহাওয়া বিভাগে দেখে নিন।",
        "soil_reply": "সয়েল হেলথ কার্ড প্রকল্পের অধীনে মাটি পরীক্ষা করিয়ে সঠিক পরিমাণে সার প্রয়োগ করুন।"
    }
}

def hal_chat_response(message: str, lang: str = "en") -> dict:
    """
    Multilingual conversational AI bot 'Hal' for KISAN AI.
    Handles Hindi, English, Punjabi, Telugu, Tamil, Bengali with domain-specific agri knowledge.
    """
    msg = message.lower().strip()
    if lang not in KB_RESPONSES:
        lang = "en"
    
    res_set = KB_RESPONSES[lang]

    # Keyword routing
    if any(k in msg for k in ["hello", "hi", "namaste", "sat sri akal", "pranam", "hey", "hal", "नमस्ते", "ਸਤਿ"]):
        reply = res_set["greeting"]
    elif any(k in msg for k in ["mandi", "price", "rate", "bhav", "cost", "दाम", "भाव", "ਰੇਟ", "ధర", "விலை", "দর"]):
        reply = res_set["mandi_reply"]
    elif any(k in msg for k in ["pm-kisan", "pm kisan", "6000", "kisan samman", "सम्मान निधि", "ਕਿਸ਼ਤ"]):
        reply = res_set["pmkisan_reply"]
    elif any(k in msg for k in ["bima", "insurance", "pmfby", "fasal bima", "बीमा", "ਬੀਮਾ", "భీమా", "காப்பீடு", "বিমা"]):
        reply = res_set["pmfby_reply"]
    elif any(k in msg for k in ["disease", "fungus", "blight", "yellow", "leaf", "pest", "कीड़ा", "बीमारी", "ਰੋਗ", "తెగులు", "நோய்", "রোগ"]):
        reply = res_set["disease_reply"]
    elif any(k in msg for k in ["weather", "rain", "temperature", "spray", "बारिश", "मौसम", "ਮੌਸਮ", "వర్షం", "வானிலை", "বৃষ্টি"]):
        reply = res_set["weather_reply"]
    elif any(k in msg for k in ["soil", "khad", "fertilizer", "urea", "मिट्टी", "खाद", "ਮਿੱਟੀ", "మట్టి", "மண்", "মাটি"]):
        reply = res_set["soil_reply"]
    elif any(k in msg for k in ["scheme", "yojana", "govt", "subsidy", "योजना", "ਸਕੀਮ", "పథకం", "திட்டம்", "প্রকল্প"]):
        reply = f"{res_set['pmkisan_reply']} Также проверьте / Also explore PMFBY, KCC, and PMKSY Micro-irrigation subsidies under the Government Schemes section."
    else:
        reply = res_set["fallback"]

    # Provide smart contextual suggestions for the user
    suggested_actions = [
        {"en": "Show Mandi Rates", "hi": "ताज़ा मंडी भाव देखें", "action": "mandi"},
        {"en": "Scan Leaf Disease", "hi": "फसल रोग पहचानें", "action": "disease"},
        {"en": "Live Weather Advisory", "hi": "मौसम और स्प्रे सलाह", "action": "weather"},
        {"en": "Govt Schemes & Subsidies", "hi": "सरकारी योजनाएं", "action": "schemes"}
    ]

    return {
        "success": True,
        "bot_name": "Hal (हल)",
        "language": lang,
        "reply": reply,
        "suggestions": [
            s.get(lang, s["en"]) for s in suggested_actions
        ]
    }
