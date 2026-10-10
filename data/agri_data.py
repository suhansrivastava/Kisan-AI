# Comprehensive Agricultural Knowledge Base for KISAN AI

DISEASE_DATABASE = {
    "tomato_early_blight": {
        "crop": "Tomato (टमाटर)",
        "disease_name": "Early Blight (Alternaria solani)",
        "severity": "Moderate to High",
        "symptoms": [
            "Concentric rings ('target board' pattern) on older lower leaves.",
            "Yellowing (chlorosis) halo around brown spots.",
            "Premature defoliation and stem collar rot in seedlings.",
            "Sunken dark leathery spots near fruit stem."
        ],
        "cause": "Fungal pathogen *Alternaria solani*, promoted by warm temperatures (24-29°C) and frequent rainfall/high humidity.",
        "chemical_treatment": [
            "Spray Mancozeb 75% WP @ 2.5 g/L or Chlorothalonil @ 2 g/L at first sign.",
            "For severe spread, apply Azoxystrobin 23% SC @ 1 ml/L or Difenoconazole 25% EC @ 0.5-1 ml/L."
        ],
        "organic_treatment": [
            "Spray Neem Seed Kernel Extract (NSKE 5%) or Trichoderma viride @ 5-10 g/L.",
            "Bordeaux mixture 1% spray as protective measure.",
            "Remove and safely burn infected lower foliage."
        ],
        "prevention": [
            "Maintain 60cm spacing for proper air circulation.",
            "Avoid overhead sprinkler irrigation; use drip irrigation.",
            "Practice 3-year crop rotation with non-solanaceous crops."
        ]
    },
    "tomato_late_blight": {
        "crop": "Tomato (टमाटर)",
        "disease_name": "Late Blight (Phytophthora infestans)",
        "severity": "Critical / Emergency",
        "symptoms": [
            "Water-soaked dark lesions appearing rapidly on leaves and petioles.",
            "White velvety fungal growth underneath leaves in high moisture conditions.",
            "Greasy dark olive-brown sunken patches on green/ripe fruit.",
            "Entire foliage turns brown, wilts and collapses within days."
        ],
        "cause": "Oomycete pathogen *Phytophthora infestans*, active in cool (15-20°C) and persistently wet/foggy conditions.",
        "chemical_treatment": [
            "Immediate foliar spray of Metalaxyl 8% + Mancozeb 64% WP (Ridomil MZ) @ 2.5 g/L.",
            "Alternate with Cymoxanil 8% + Mancozeb 64% WP @ 2 g/L or Dimethomorph @ 1.5 g/L."
        ],
        "organic_treatment": [
            "Copper oxychloride 50% WP @ 3 g/L.",
            "Prune infected plant parts immediately; avoid working in wet fields to prevent spore spread."
        ],
        "prevention": [
            "Plant certified disease-free and resistant cultivars (e.g., Arka Rakshak, Kashi Amrit).",
            "Ensure ridge-and-furrow planting with excellent drainage."
        ]
    },
    "potato_late_blight": {
        "crop": "Potato (आलू)",
        "disease_name": "Late Blight (Phytophthora infestans)",
        "severity": "High",
        "symptoms": [
            "Water-soaked pale spots enlarging quickly to purplish-brown lesions.",
            "White fungal mold on undersides of leaves during misty mornings.",
            "Brown granular dry rot in tubers beneath skin."
        ],
        "cause": "Humid conditions (>90% RH) and cool temperatures (12-22°C).",
        "chemical_treatment": [
            "Prophylactic: Mancozeb 75% WP @ 2.5 g/L.",
            "Curative: Metalaxyl-M + Mancozeb @ 2.5 g/L or Fenamidone + Mancozeb @ 2 g/L."
        ],
        "organic_treatment": [
            "Copper hydroxide @ 2 g/L spray.",
            "Earthing up tubers well (minimum 10-15 cm soil cover) to prevent spore wash-down."
        ],
        "prevention": [
            "Use certified seed tubers.",
            "Destroy potato cull piles before sowing season."
        ]
    },
    "wheat_yellow_rust": {
        "crop": "Wheat (गेहूं)",
        "disease_name": "Yellow / Stripe Rust (Puccinia striiformis)",
        "severity": "High",
        "symptoms": [
            "Bright yellowish-orange linear pustules arranged in stripes along leaf veins.",
            "Powdery yellow spores rubbing off onto clothes and fingers.",
            "Stunted grain filling and shriveled kernels."
        ],
        "cause": "Fungus *Puccinia striiformis*, favored by cool humid weather (10-15°C) and morning dew.",
        "chemical_treatment": [
            "Foliar spray of Propiconazole 25% EC (Tilt) @ 1 ml/L or Tebuconazole @ 1 ml/L as soon as yellow pustules appear.",
            "Repeat after 15 days if stripe development persists."
        ],
        "organic_treatment": [
            "Cow urine fermented solution (1:10) spray in early stages.",
            "Sulfur 80% WDG @ 3 g/L."
        ],
        "prevention": [
            "Sow rust-resistant varieties like HD 2967, DBW 187, DBW 303, PBW 550.",
            "Avoid excessive nitrogen fertilization."
        ]
    },
    "rice_blast": {
        "crop": "Rice / Paddy (धान)",
        "disease_name": "Rice Blast (Magnaporthe oryzae)",
        "severity": "High",
        "symptoms": [
            "Spindle-shaped / diamond-shaped lesions with grayish centers and dark brown margins on leaves.",
            "Node rot causing culm breakage.",
            "Neck blast turning panicle neck black-brown, causing chaffy, empty grains."
        ],
        "cause": "Airborne spores under high nitrogen, cool nights (20°C), and relative humidity >90%.",
        "chemical_treatment": [
            "Tricyclazole 75% WP (Beam) @ 0.6 g/L or Isoprothiolane 40% EC @ 1.5 ml/L.",
            "Spray at tillering and boot leaf emergence stages."
        ],
        "organic_treatment": [
            "Pseudomonas fluorescens foliar spray @ 5 g/L or seed treatment @ 10 g/kg.",
            "Neem oil 3000 ppm @ 3 ml/L."
        ],
        "prevention": [
            "Split application of Nitrogen fertilizer; do not apply excessive urea at once.",
            "Burn or compost infected stubble after harvest."
        ]
    },
    "cotton_leaf_curl": {
        "crop": "Cotton (कपास)",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV)",
        "severity": "Moderate to High",
        "symptoms": [
            "Upward or downward leaf curling with thick swollen leaf veins.",
            "Enation (small cup-like leaf outgrowths) on underside of main veins.",
            "Stunted plant growth and severely reduced boll setting."
        ],
        "cause": "Begomovirus transmitted by Whiteflies (*Bemisia tabaci*).",
        "chemical_treatment": [
            "Vector Control: Imidacloprid 17.8% SL @ 0.5 ml/L or Diafenthiuron 50% WP @ 1.2 g/L.",
            "Alternate with Pyriproxyfen 10% EC @ 2 ml/L or Flonicamid 50% WG @ 0.3 g/L."
        ],
        "organic_treatment": [
            "Yellow sticky traps (15-20 per acre) to trap whitefly vectors.",
            "Neem oil spray (10,000 ppm) @ 2 ml/L every 10 days."
        ],
        "prevention": [
            "Eradicate weed hosts like Abutilon and Parthenium near farm borders.",
            "Plant CLCuV tolerant Bt-cotton hybrids."
        ]
    },
    "healthy": {
        "crop": "Crops (फसल)",
        "disease_name": "Healthy Plant (स्वस्थ पौधा)",
        "severity": "None - Optimal Condition",
        "symptoms": [
            "Vibrant green pigmentation with uniform foliage.",
            "No necrotic spots, chlorosis, curling, or fungal pustules.",
            "Strong turgidity, vigorous growth nodes and root system."
        ],
        "cause": "Optimal soil nutrition, proper irrigation, and pest management.",
        "chemical_treatment": [
            "No chemical fungicides or pesticides required."
        ],
        "organic_treatment": [
            "Maintain soil vitality with vermicompost (2 tons/acre) and Jeevamrutha foliar spray.",
            "Ensure regular mulching to preserve beneficial soil microbiome."
        ],
        "prevention": [
            "Continue periodic field scouting once a week.",
            "Adhere to balanced NPK ratios according to Soil Health Card guidelines."
        ]
    }
}

SCHEMES_DATABASE = [
    {
        "id": "pm-kisan",
        "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "category": "Direct Income Support",
        "ministry": "Ministry of Agriculture & Farmers Welfare, Govt of India",
        "benefit": "₹6,000 per year directly into bank account in 3 equal installments of ₹2,000.",
        "eligibility": "All landholding farmer families across India (subject to standard exclusion criteria like institutional landholders).",
        "documents": ["Aadhaar Card", "Land Ownership Documents (Khata/Khasra/ROR)", "Bank Account linked with Aadhaar", "Mobile number linked with Aadhaar"],
        "portal_url": "https://pmkisan.gov.in",
        "helpline": "155261 / 011-24300606",
        "description": "Central Sector scheme providing financial assistance to cultivate crops, purchase seeds/fertilizers, and handle domestic needs."
    },
    {
        "id": "pmfby",
        "name": "PMFBY (Pradhan Mantri Fasal Bima Yojana)",
        "category": "Crop Insurance",
        "ministry": "Ministry of Agriculture & Farmers Welfare",
        "benefit": "Comprehensive financial protection against non-preventable natural risks (drought, flood, pests, unseasonal hail). Farmers pay only 2% premium for Kharif, 1.5% for Rabi, and 5% for commercial/horticultural crops.",
        "eligibility": "All farmers including sharecroppers and tenant farmers growing notified crops in notified areas.",
        "documents": ["Crop Sowing Certificate / Patwari report", "Land Record (Pahani/Adangal)", "Bank Passbook", "Aadhaar Card"],
        "portal_url": "https://pmfby.gov.in",
        "helpline": "1800 180 1551 (Kisan Call Centre)",
        "description": "Flagship crop insurance scheme ensuring income stabilization during catastrophic weather events and localized calamities."
    },
    {
        "id": "kcc",
        "name": "Kisan Credit Card (KCC) Scheme",
        "category": "Subsidized Credit",
        "ministry": "Reserve Bank of India & NABARD",
        "benefit": "Collateral-free agricultural loans up to ₹1.60 Lakh (and up to ₹3 Lakh at effectively 4% interest rate with prompt repayment incentive).",
        "eligibility": "Individual farmers, joint borrowers, tenant farmers, self-help groups (SHGs), and joint liability groups (JLGs).",
        "documents": ["Land records / tenancy agreement", "Identity & Address proof (Aadhaar/Voter ID)", "Passport photos"],
        "portal_url": "https://www.nabard.org",
        "helpline": "1800 22 9090",
        "description": "Adequate and timely credit support from the banking system for cultivation, post-harvest expenses, and farm asset maintenance."
    },
    {
        "id": "pmksy",
        "name": "PMKSY (Per Drop More Crop - PM Krishi Sinchayee)",
        "category": "Irrigation & Water Tech",
        "ministry": "Ministry of Jal Shakti & Dept of Agriculture",
        "benefit": "Up to 55% subsidy for small and marginal farmers (45% for other farmers) for micro-irrigation systems (Drip & Sprinkler).",
        "eligibility": "Farmers owning agricultural land with assured irrigation water source.",
        "documents": ["Land ownership documents", "Soil & Water testing report (if applicable)", "Bank account details", "Aadhaar"],
        "portal_url": "https://pmksy.gov.in",
        "helpline": "011-23381012",
        "description": "Enhancing water use efficiency through modern precision irrigation systems to expand farm yields per water droplet."
    },
    {
        "id": "soil-health-card",
        "name": "Soil Health Card Scheme",
        "category": "Soil Testing & Fertility",
        "ministry": "Department of Agriculture and Farmers Welfare",
        "benefit": "Free lab assessment of soil nutrient status (12 parameters: N, P, K, S, Zn, Fe, Cu, Mn, Bo, pH, EC, OC) with tailored fertilizer dosage recommendations.",
        "eligibility": "All agricultural landowners across all states and union territories.",
        "documents": ["Soil sample from plot", "Farmer ID / Aadhaar", "Khasra Number"],
        "portal_url": "https://soilhealth.dac.gov.in",
        "helpline": "011-24305548",
        "description": "Helps farmers optimize fertilizer input, cut expenditure on excess urea, and preserve long-term soil microbial health."
    },
    {
        "id": "e-nam",
        "name": "e-NAM (National Agriculture Market)",
        "category": "Digital Mandi & Trading",
        "ministry": "Small Farmers Agribusiness Consortium (SFAC)",
        "benefit": "Pan-India electronic trading portal networking existing APMC mandis to create a unified national market for commodities with transparent online bidding.",
        "eligibility": "Registered farmers, traders, and FPOs across 1,361+ linked mandis.",
        "documents": ["Bank Details", "Aadhaar / Mobile number", "APMC registration receipt"],
        "portal_url": "https://enam.gov.in",
        "helpline": "1800 270 0224",
        "description": "Eliminates intermediaries, gives access to nationwide buyers, and facilitates quality-based electronic assaying."
    },
    {
        "id": "paramparagat-krishi",
        "name": "PKVY (Paramparagat Krishi Vikas Yojana)",
        "category": "Organic Farming Support",
        "ministry": "Ministry of Agriculture & Farmers Welfare",
        "benefit": "Financial assistance of ₹50,000 per hectare for 3 years, of which ₹31,000 is given directly for organic inputs (bio-fertilizers, seeds, vermicompost).",
        "eligibility": "Farmers forming clusters of 50 or more farmers having 50 acres land.",
        "documents": ["Cluster formation documents", "Aadhaar", "Bank Account", "Land records"],
        "portal_url": "https://pgsindia-ncof.gov.in",
        "helpline": "0120-2764906",
        "description": "Supports commercial organic production via Participatory Guarantee System (PGS) certification and direct market linkage."
    },
    {
        "id": "sub-mission-agri-mechanization",
        "name": "SMAM (Sub-Mission on Agricultural Mechanization)",
        "category": "Farm Machinery & Tractor Subsidy",
        "ministry": "Ministry of Agriculture & Farmers Welfare",
        "benefit": "40% to 50% subsidy on procurement of tractors, power tillers, rotavators, harvesters, and establishment of Custom Hiring Centres (CHC).",
        "eligibility": "Small, marginal, SC/ST, and women farmers given preference.",
        "documents": ["Aadhaar", "Land records (Khatauni)", "Bank Passbook", "Caste certificate (if applicable)"],
        "portal_url": "https://agrimachinery.nic.in",
        "helpline": "1800 180 1551",
        "description": "Increases farm productivity by bringing modern mechanized implements within reach of smallholder farming families."
    }
]

IMPORTANT_WEBSITES = [
    {
        "title": "e-NAM (National Agriculture Market)",
        "category": "Mandi Trading & Real-time Prices",
        "url": "https://enam.gov.in",
        "badge": "Central Portal",
        "desc": "Official unified platform for interstate mandi auctions, price discovery, and digital payments."
    },
    {
        "title": "Agmarknet (Agricultural Marketing Information Network)",
        "category": "Price Statistics & Commodity Trends",
        "url": "https://agmarknet.gov.in",
        "badge": "Price Data",
        "desc": "Government portal with daily arrival quantities, minimum, maximum, and modal wholesale rates across 3000+ mandis."
    },
    {
        "title": "PM-KISAN Official Portal",
        "category": "Direct Benefit Transfer",
        "url": "https://pmkisan.gov.in",
        "badge": "DBT Benefit",
        "desc": "Check installment status, e-KYC verification, new farmer registration, and beneficiary list."
    },
    {
        "title": "PM Fasal Bima Yojana (PMFBY)",
        "category": "Crop Insurance",
        "url": "https://pmfby.gov.in",
        "badge": "Insurance Claims",
        "desc": "Calculate insurance premium, submit loss reports within 72 hours, and track policy status."
    },
    {
        "title": "ICAR (Indian Council of Agricultural Research)",
        "category": "Research & Advisory",
        "url": "https://icar.org.in",
        "badge": "Scientific Research",
        "desc": "Apex body for coordinating agricultural education and research with advisory bulletins across all agro-climatic zones."
    },
    {
        "title": "IMD Mausam & Agromet Advisory",
        "category": "Weather & Monsoon Forecast",
        "url": "https://mausam.imd.gov.in",
        "badge": "Meteorological Data",
        "desc": "India Meteorological Department district-level agromet weather bulletins and Doppler radar updates."
    },
    {
        "title": "Kisan Suvidha Portal",
        "category": "Unified Farmer Services",
        "url": "https://kisansuvidha.gov.in",
        "badge": "Multi-Service",
        "desc": "One-stop national portal for weather, market prices, plant protection, and dealer locating."
    },
    {
        "title": "Soil Health Card Portal",
        "category": "Soil Testing",
        "url": "https://soilhealth.dac.gov.in",
        "badge": "Soil Fertility",
        "desc": "Sample test tracking, card download, and customized micro-nutrient recommendations."
    }
]

MANDI_PRICE_DATA = [
    {
        "id": 1,
        "commodity": "Wheat (गेहूं)",
        "category": "Cereals",
        "variety": "Sharbati / Lok-1",
        "mandi": "Indore Mandi",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "min_price": 2420,
        "max_price": 2850,
        "modal_price": 2680,
        "unit": "₹ / Quintal",
        "arrival_today": "3,450 Quintals",
        "price_change": "+₹40",
        "trend": "up",
        "msp": 2425
    },
    {
        "id": 2,
        "commodity": "Wheat (गेहूं)",
        "category": "Cereals",
        "variety": "HD-2967",
        "mandi": "Khanna Mandi",
        "district": "Ludhiana",
        "state": "Punjab",
        "min_price": 2425,
        "max_price": 2550,
        "modal_price": 2470,
        "unit": "₹ / Quintal",
        "arrival_today": "5,120 Quintals",
        "price_change": "+₹15",
        "trend": "up",
        "msp": 2425
    },
    {
        "id": 3,
        "commodity": "Paddy / Rice (बासमती धान)",
        "category": "Cereals",
        "variety": "1121 Pusa Basmati",
        "mandi": "Karnal Mandi",
        "district": "Karnal",
        "state": "Haryana",
        "min_price": 3800,
        "max_price": 4350,
        "modal_price": 4150,
        "unit": "₹ / Quintal",
        "arrival_today": "2,890 Quintals",
        "price_change": "+₹75",
        "trend": "up",
        "msp": 2300
    },
    {
        "id": 4,
        "commodity": "Paddy / Rice (धान कॉमन)",
        "category": "Cereals",
        "variety": "Common Paddy",
        "mandi": "Burdwan Mandi",
        "district": "Purba Bardhaman",
        "state": "West Bengal",
        "min_price": 2250,
        "max_price": 2380,
        "modal_price": 2320,
        "unit": "₹ / Quintal",
        "arrival_today": "4,200 Quintals",
        "price_change": "-₹10",
        "trend": "down",
        "msp": 2300
    },
    {
        "id": 5,
        "commodity": "Tomato (टमाटर)",
        "category": "Vegetables",
        "variety": "Hybrid Red",
        "mandi": "Kolar Mandi",
        "district": "Kolar",
        "state": "Karnataka",
        "min_price": 1400,
        "max_price": 2200,
        "modal_price": 1850,
        "unit": "₹ / Quintal",
        "arrival_today": "7,800 Quintals",
        "price_change": "-₹120",
        "trend": "down",
        "msp": None
    },
    {
        "id": 6,
        "commodity": "Tomato (टमाटर)",
        "category": "Vegetables",
        "variety": "Desi / Local",
        "mandi": "Azadpur Mandi",
        "district": "North Delhi",
        "state": "Delhi",
        "min_price": 1600,
        "max_price": 2400,
        "modal_price": 2100,
        "unit": "₹ / Quintal",
        "arrival_today": "9,400 Quintals",
        "price_change": "+₹90",
        "trend": "up",
        "msp": None
    },
    {
        "id": 7,
        "commodity": "Onion (प्याज)",
        "category": "Vegetables",
        "variety": "Red Garwa",
        "mandi": "Lasalgaon Mandi",
        "district": "Nashik",
        "state": "Maharashtra",
        "min_price": 1900,
        "max_price": 2750,
        "modal_price": 2450,
        "unit": "₹ / Quintal",
        "arrival_today": "14,500 Quintals",
        "price_change": "+₹60",
        "trend": "up",
        "msp": None
    },
    {
        "id": 8,
        "commodity": "Potato (आलू)",
        "category": "Vegetables",
        "variety": "Jyoti / Pukhraj",
        "mandi": "Agra Mandi",
        "district": "Agra",
        "state": "Uttar Pradesh",
        "min_price": 1250,
        "max_price": 1650,
        "modal_price": 1480,
        "unit": "₹ / Quintal",
        "arrival_today": "11,200 Quintals",
        "price_change": "+₹20",
        "trend": "up",
        "msp": None
    },
    {
        "id": 9,
        "commodity": "Cotton (कपास)",
        "category": "Fiber Crops",
        "variety": "Medium Long Staple",
        "mandi": "Rajkot Mandi",
        "district": "Rajkot",
        "state": "Gujarat",
        "min_price": 6800,
        "max_price": 7550,
        "modal_price": 7250,
        "unit": "₹ / Quintal",
        "arrival_today": "3,100 Quintals",
        "price_change": "-₹50",
        "trend": "down",
        "msp": 7121
    },
    {
        "id": 10,
        "commodity": "Soybean (सोयाबीन)",
        "category": "Oilseeds",
        "variety": "Yellow JS-9560",
        "mandi": "Ujjain Mandi",
        "district": "Ujjain",
        "state": "Madhya Pradesh",
        "min_price": 4400,
        "max_price": 4920,
        "modal_price": 4750,
        "unit": "₹ / Quintal",
        "arrival_today": "4,700 Quintals",
        "price_change": "+₹45",
        "trend": "up",
        "msp": 4892
    },
    {
        "id": 11,
        "commodity": "Mustard (सरसों)",
        "category": "Oilseeds",
        "variety": "Pusa Bold",
        "mandi": "Bharatpur Mandi",
        "district": "Bharatpur",
        "state": "Rajasthan",
        "min_price": 5400,
        "max_price": 5950,
        "modal_price": 5780,
        "unit": "₹ / Quintal",
        "arrival_today": "2,400 Quintals",
        "price_change": "+₹30",
        "trend": "up",
        "msp": 5650
    },
    {
        "id": 12,
        "commodity": "Gram / Chana (चना)",
        "category": "Pulses",
        "variety": "Desi Chana",
        "mandi": "Akola Mandi",
        "district": "Akola",
        "state": "Maharashtra",
        "min_price": 5800,
        "max_price": 6450,
        "modal_price": 6200,
        "unit": "₹ / Quintal",
        "arrival_today": "1,950 Quintals",
        "price_change": "+₹80",
        "trend": "up",
        "msp": 5440
    },
    {
        "id": 13,
        "commodity": "Sugarcane (गन्ना)",
        "category": "Commercial",
        "variety": "Co 0238",
        "mandi": "Muzaffarnagar",
        "district": "Muzaffarnagar",
        "state": "Uttar Pradesh",
        "min_price": 360,
        "max_price": 395,
        "modal_price": 375,
        "unit": "₹ / Quintal",
        "arrival_today": "18,000 Quintals",
        "price_change": "0",
        "trend": "stable",
        "msp": 340
    },
    {
        "id": 14,
        "commodity": "Maize / Corn (मक्का)",
        "category": "Cereals",
        "variety": "Yellow Hybrid",
        "mandi": "Gulabbagh Mandi",
        "district": "Purnia",
        "state": "Bihar",
        "min_price": 2050,
        "max_price": 2350,
        "modal_price": 2240,
        "unit": "₹ / Quintal",
        "arrival_today": "3,800 Quintals",
        "price_change": "-₹15",
        "trend": "down",
        "msp": 2090
    }
]

LOCATIONS_DATABASE = {
    "Delhi": {"lat": 28.6139, "lon": 77.2090, "state": "Delhi", "soil": "Alluvial, Loamy"},
    "Indore": {"lat": 22.7196, "lon": 75.8577, "state": "Madhya Pradesh", "soil": "Deep Black Cotton Soil"},
    "Ludhiana": {"lat": 30.9010, "lon": 75.8573, "state": "Punjab", "soil": "Alluvial Loam, Highly Fertile"},
    "Karnal": {"lat": 29.6857, "lon": 76.9905, "state": "Haryana", "soil": "Clayey Alluvial Soil"},
    "Nashik": {"lat": 19.9975, "lon": 73.7898, "state": "Maharashtra", "soil": "Black Basaltic Soil & Red Loam"},
    "Agra": {"lat": 27.1767, "lon": 78.0081, "state": "Uttar Pradesh", "soil": "Sandy Loam to Clayey Loam"},
    "Rajkot": {"lat": 22.3039, "lon": 70.8022, "state": "Gujarat", "soil": "Medium Black Cotton Soil"},
    "Kolar": {"lat": 13.1367, "lon": 78.1291, "state": "Karnataka", "soil": "Red Sandy Loam"},
    "Varanasi": {"lat": 25.3176, "lon": 82.9739, "state": "Uttar Pradesh", "soil": "Gangetic Alluvial Silt"},
    "Patna": {"lat": 25.5941, "lon": 85.1376, "state": "Bihar", "soil": "Old Gangetic Alluvium (Bangar)"},
    "Jaipur": {"lat": 26.9124, "lon": 75.7873, "state": "Rajasthan", "soil": "Sandy Desert Soil / Aridisols"},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867, "state": "Telangana", "soil": "Red Chalkas & Black Earth"},
    "Nagpur": {"lat": 21.1458, "lon": 79.0882, "state": "Maharashtra", "soil": "Deep Black Regur Soil"}
}
