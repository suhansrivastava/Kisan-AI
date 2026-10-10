// KISAN AI Frontend Client Logic

let currentLanguage = 'en';

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initCropDiagnosis();
    initMandiFilters();
    initWeather();
    initChatHal();
    initLanguageSelector();
});

// Tab Switching
function initNavigation() {
    const tabs = document.querySelectorAll('.nav-tab-btn');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.getAttribute('data-target');
            document.querySelectorAll('.nav-tab-btn').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content-panel').forEach(p => p.classList.remove('active'));
            
            tab.classList.add('active');
            const targetPanel = document.getElementById(targetId);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }
        });
    });
}

function switchTab(tabId) {
    const targetTab = document.querySelector(`.nav-tab-btn[data-target="${tabId}"]`);
    if (targetTab) {
        targetTab.click();
    }
}

// Language Switcher
function initLanguageSelector() {
    const select = document.getElementById('global-lang-select');
    if (!select) return;
    
    select.addEventListener('change', (e) => {
        currentLanguage = e.target.value;
        const halLang = document.getElementById('hal-lang-select');
        if (halLang) {
            halLang.value = currentLanguage;
        }
        // Notify user in chat
        sendBotGreeting(currentLanguage);
    });
}

// --- MODULE 1: Crop Disease Detection ---
let selectedFile = null;

function initCropDiagnosis() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('crop-file-input');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const btnDiagnose = document.getElementById('btn-diagnose');
    const resetBtn = document.getElementById('btn-reset-upload');

    if (!dropZone || !fileInput) return;

    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFileSelect(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
            handleFileSelect(e.target.files[0]);
        }
    });

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            selectedFile = null;
            fileInput.value = '';
            previewContainer.style.display = 'none';
            dropZone.style.display = 'block';
            document.getElementById('diagnosis-empty').style.display = 'block';
            document.getElementById('diagnosis-result').style.display = 'none';
        });
    }

    if (btnDiagnose) {
        btnDiagnose.addEventListener('click', executeDiagnosis);
    }
}

function handleFileSelect(file) {
    selectedFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        const preview = document.getElementById('image-preview');
        const container = document.getElementById('preview-container');
        const dropZone = document.getElementById('drop-zone');
        preview.src = e.target.result;
        container.style.display = 'block';
        dropZone.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

// Preset samples loader
async function loadSampleCrop(sampleKey, cropType) {
    document.getElementById('crop-type-select').value = cropType;
    
    // Create an inline SVG image for the sample representation to upload
    const svgData = generateSampleSVG(sampleKey);
    const blob = new Blob([svgData], { type: 'image/svg+xml' });
    selectedFile = new File([blob], `${sampleKey}_sample.svg`, { type: 'image/svg+xml' });
    
    const preview = document.getElementById('image-preview');
    const container = document.getElementById('preview-container');
    const dropZone = document.getElementById('drop-zone');
    preview.src = URL.createObjectURL(blob);
    container.style.display = 'block';
    dropZone.style.display = 'none';

    executeDiagnosis();
}

function generateSampleSVG(key) {
    let mainColor = '#15803d';
    let spotColor = '#78350f';
    let spots = '';

    if (key.includes('blight')) {
        mainColor = '#4d7c0f';
        spotColor = '#3e2723';
        spots = `
            <circle cx="80" cy="90" r="24" fill="${spotColor}" opacity="0.85"/>
            <circle cx="150" cy="130" r="32" fill="${spotColor}" opacity="0.9"/>
            <circle cx="120" cy="180" r="18" fill="#ca8a04" opacity="0.8"/>
        `;
    } else if (key.includes('rust')) {
        mainColor = '#84cc16';
        spotColor = '#d97706';
        spots = `
            <rect x="50" y="40" width="12" height="150" rx="6" fill="${spotColor}" opacity="0.9"/>
            <rect x="90" y="60" width="10" height="130" rx="5" fill="${spotColor}" opacity="0.85"/>
            <rect x="130" y="50" width="14" height="140" rx="7" fill="${spotColor}" opacity="0.95"/>
        `;
    } else {
        mainColor = '#16a34a';
        spots = `<circle cx="100" cy="100" r="6" fill="#15803d"/>`;
    }

    return `
    <svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
        <rect width="256" height="256" fill="#f8fafc"/>
        <path d="M128,20 C180,60 210,120 180,200 C150,230 100,230 70,200 C40,120 70,60 128,20 Z" fill="${mainColor}"/>
        <line x1="128" y1="20" x2="128" y2="220" stroke="#166534" stroke-width="3"/>
        ${spots}
    </svg>`;
}

async function executeDiagnosis() {
    if (!selectedFile) {
        alert('Please choose or drag-and-drop a crop photo first.');
        return;
    }

    const btn = document.getElementById('btn-diagnose');
    const originalText = btn.innerHTML;
    btn.innerHTML = 'Analyzing Foliage...';
    btn.disabled = true;

    const cropType = document.getElementById('crop-type-select').value;
    const formData = new FormData();
    formData.append('image', selectedFile);
    formData.append('crop_type', cropType);

    try {
        const resp = await fetch('/api/diagnose', {
            method: 'POST',
            body: formData
        });
        const data = await resp.json();

        if (data.success) {
            renderDiagnosisResults(data);
        } else {
            alert('Analysis error: ' + (data.error || 'Unknown issue'));
        }
    } catch (e) {
        alert('Failed to connect to diagnostic server: ' + e.message);
    } finally {
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
}

function renderDiagnosisResults(data) {
    document.getElementById('diagnosis-empty').style.display = 'none';
    const resultBox = document.getElementById('diagnosis-result');
    resultBox.style.display = 'block';

    document.getElementById('res-crop-name').innerText = data.crop;
    document.getElementById('res-disease-name').innerText = data.disease_name;
    document.getElementById('res-confidence').innerText = `${data.confidence}% Confidence`;
    
    // Severity badge
    const badge = document.getElementById('res-severity-badge');
    badge.innerText = data.severity;
    badge.className = 'badge-severity';
    if (data.severity.toLowerCase().includes('high') || data.severity.toLowerCase().includes('critical')) {
        badge.classList.add('badge-high');
    } else if (data.severity.toLowerCase().includes('moderate')) {
        badge.classList.add('badge-mod');
    } else {
        badge.classList.add('badge-healthy');
    }

    // Cause & symptoms
    document.getElementById('res-cause').innerText = data.cause;
    const symptomsUl = document.getElementById('res-symptoms-list');
    symptomsUl.innerHTML = data.symptoms.map(s => `<li>${s}</li>`).join('');

    // Treatments
    const chemUl = document.getElementById('res-chemical-list');
    chemUl.innerHTML = data.chemical_treatment.map(t => `<li>${t}</li>`).join('');

    const orgUl = document.getElementById('res-organic-list');
    orgUl.innerHTML = data.organic_treatment.map(t => `<li>${t}</li>`).join('');

    const prevUl = document.getElementById('res-prevention-list');
    prevUl.innerHTML = data.prevention.map(p => `<li>${p}</li>`).join('');

    // Visual metrics
    if (data.visual_metrics) {
        const vm = data.visual_metrics;
        document.getElementById('bar-green').style.width = `${vm.green_foliage_pct}%`;
        document.getElementById('bar-yellow').style.width = `${vm.chlorosis_yellow_pct}%`;
        document.getElementById('bar-brown').style.width = `${vm.necrotic_brown_pct}%`;
        document.getElementById('bar-dark').style.width = `${vm.dark_blight_pct}%`;

        document.getElementById('val-green').innerText = `${vm.green_foliage_pct}%`;
        document.getElementById('val-yellow').innerText = `${vm.chlorosis_yellow_pct}%`;
        document.getElementById('val-brown').innerText = `${vm.necrotic_brown_pct}%`;
        document.getElementById('val-dark').innerText = `${vm.dark_blight_pct}%`;
    }
}

// --- MODULE 2: Mandi Prices Filtering ---
function initMandiFilters() {
    const searchInput = document.getElementById('mandi-search');
    const stateFilter = document.getElementById('mandi-state-filter');
    const categoryFilter = document.getElementById('mandi-category-filter');

    const triggerFetch = () => {
        const q = searchInput ? searchInput.value : '';
        const state = stateFilter ? stateFilter.value : '';
        const cat = categoryFilter ? categoryFilter.value : '';

        fetch(`/api/mandi-rates?q=${encodeURIComponent(q)}&state=${encodeURIComponent(state)}&commodity=${encodeURIComponent(cat)}`)
            .then(res => res.json())
            .then(res => {
                if (res.success) {
                    renderMandiRows(res.data);
                }
            })
            .catch(err => console.error("Mandi rate error:", err));
    };

    if (searchInput) searchInput.addEventListener('input', triggerFetch);
    if (stateFilter) stateFilter.addEventListener('change', triggerFetch);
    if (categoryFilter) categoryFilter.addEventListener('change', triggerFetch);
}

function renderMandiRows(records) {
    const tbody = document.getElementById('mandi-tbody');
    if (!tbody) return;

    if (records.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 24px; color: #64748b;">No matching mandi commodities found.</td></tr>`;
        return;
    }

    tbody.innerHTML = records.map(item => `
        <tr>
            <td>
                <strong>${item.commodity}</strong><br>
                <small style="color:#64748b;">Variety: ${item.variety}</small>
            </td>
            <td>
                <span>${item.mandi}</span><br>
                <small style="color:#64748b;">${item.district}, ${item.state}</small>
            </td>
            <td>₹${item.min_price}</td>
            <td>₹${item.max_price}</td>
            <td>
                <span class="price-modal-val">₹${item.modal_price}</span>
                <small style="display:block; color:#64748b; font-size:0.75rem;">${item.unit}</small>
            </td>
            <td>
                <span class="trend-badge ${item.trend}">
                    ${item.trend === 'up' ? '▲' : (item.trend === 'down' ? '▼' : '●')} ${item.price_change}
                </span>
            </td>
            <td>
                <span style="font-size:0.85rem; font-weight:600;">${item.msp ? '₹' + item.msp : 'Market Driven'}</span>
            </td>
        </tr>
    `).join('');
}

// --- MODULE 3: Weather & Agromet Advisory ---
function initWeather() {
    const citySelect = document.getElementById('weather-city-select');
    if (!citySelect) return;

    citySelect.addEventListener('change', () => {
        loadWeatherData(citySelect.value);
    });

    // Initial load
    loadWeatherData(citySelect.value || 'Indore');
}

async function loadWeatherData(city) {
    const spinner = document.getElementById('weather-loading');
    if (spinner) spinner.style.display = 'block';

    try {
        const resp = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
        const data = await resp.json();
        renderWeatherDetails(data);
    } catch (e) {
        console.error("Weather fetch failed:", e);
    } finally {
        if (spinner) spinner.style.display = 'none';
    }
}

function renderWeatherDetails(data) {
    document.getElementById('weather-city-display').innerText = `${data.city}, ${data.state}`;
    document.getElementById('weather-temp-display').innerText = `${Math.round(data.current.temperature)}°C`;
    document.getElementById('weather-cond-display').innerText = `${data.current.icon} ${data.current.condition}`;
    document.getElementById('weather-humidity-display').innerText = `${data.current.humidity}%`;
    document.getElementById('weather-wind-display').innerText = `${data.current.wind_speed} km/h`;
    document.getElementById('weather-soil-display').innerText = data.soil_type;

    // Advisory callouts
    const sprayBox = document.getElementById('advisory-spray-box');
    sprayBox.innerHTML = `
        <strong>${data.agri_advisory.spray_status}</strong>: ${data.agri_advisory.spray_advice}
    `;

    document.getElementById('advisory-irrigation-box').innerText = data.agri_advisory.irrigation_advice;
    document.getElementById('advisory-fungal-box').innerText = data.agri_advisory.disease_risk;

    // Daily 7-day cards
    const grid = document.getElementById('forecast-grid');
    if (grid && data.daily_forecast) {
        grid.innerHTML = data.daily_forecast.map(day => `
            <div class="forecast-mini-card">
                <div style="font-size:0.8rem; font-weight:700; color:#64748b; margin-bottom:4px;">${day.date}</div>
                <div style="font-size:24px; margin:4px 0;">${day.icon}</div>
                <div style="font-weight:700; font-size:0.95rem;">${Math.round(day.temp_max)}° / ${Math.round(day.temp_min)}°</div>
                <div style="font-size:0.75rem; color:#0284c7; margin-top:4px;">💧 ${day.rain_prob}% Rain</div>
            </div>
        `).join('');
    }
}

// --- MODULE 4: Hal Multilingual AI Chatbot ---
function initChatHal() {
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('btn-send-chat');
    const halLangSelect = document.getElementById('hal-lang-select');

    if (halLangSelect) {
        halLangSelect.addEventListener('change', (e) => {
            currentLanguage = e.target.value;
            const globalLang = document.getElementById('global-lang-select');
            if (globalLang) globalLang.value = currentLanguage;
            sendBotGreeting(currentLanguage);
        });
    }

    if (sendBtn && input) {
        sendBtn.addEventListener('click', () => submitChatMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') submitChatMessage();
        });
    }
}

function sendBotGreeting(lang) {
    const greetings = {
        en: "Hello farmer! I am Hal, your AI Farming Assistant. How may I assist you today with crops, mandi prices, weather, or government schemes?",
        hi: "नमस्ते किसान भाई! मैं 'हल' (Hal) हूँ, आपका डिजिटल कृषि साथी। फसल बीमारी, मंडी भाव या योजनाओं के बारे में पूछिए।",
        pa: "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ! ਮੈਂ 'ਹਲ' (Hal) ਹਾਂ। ਫਸਲ ਦੀ ਬਿਮਾਰੀ ਜਾਂ ਮੰਡੀ ਦੇ ਭਾਅ ਬਾਰੇ ਕੀ ਜਾਣਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        te: "నమస్కారం! నేను 'హల్' (Hal), KISAN AI సహాయకుడిని. మీకు పంటలు లేదా పథకాల గురించి ఏం సహాయం కావాలి?",
        ta: "வணக்கம்! நான் 'ஹல்' (Hal). பயிர் நோய்கள், மண்டி விலை அல்லது அரசு திட்டங்கள் குறித்து கேளுங்கள்.",
        bn: "নমস্কার! আমি 'হল' (Hal)। ফসলের রোগ, মান্ডি দর বা সরকারি প্রকল্প নিয়ে কী জানতে চান?"
    };

    appendChatMessage(greetings[lang] || greetings['en'], 'bot');
}

async function submitChatMessage(customText) {
    const input = document.getElementById('chat-input');
    const text = customText || (input ? input.value.trim() : '');
    if (!text) return;

    if (input && !customText) input.value = '';

    appendChatMessage(text, 'user');

    const halLang = document.getElementById('hal-lang-select');
    const lang = halLang ? halLang.value : currentLanguage;

    try {
        const resp = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, lang: lang })
        });
        const data = await resp.json();

        if (data.success) {
            appendChatMessage(data.reply, 'bot');
            renderChatSuggestions(data.suggestions);
        } else {
            appendChatMessage("Sorry, I could not process that request. Please try again.", 'bot');
        }
    } catch (e) {
        appendChatMessage("Connection issue with Hal assistant. Please check server.", 'bot');
    }
}

function appendChatMessage(msg, sender) {
    const messagesArea = document.getElementById('chat-messages');
    if (!messagesArea) return;

    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${sender}`;
    bubble.innerHTML = msg;

    messagesArea.appendChild(bubble);
    messagesArea.scrollTop = messagesArea.scrollHeight;
}

function renderChatSuggestions(suggestions) {
    const container = document.getElementById('chat-quick-suggestions');
    if (!container || !suggestions) return;

    container.innerHTML = suggestions.map(s => `
        <button class="preset-chip-btn" onclick="submitChatMessage('${s}')">${s}</button>
    `).join('');
}
