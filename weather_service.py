import urllib.request
import json
from data.agri_data import LOCATIONS_DATABASE

WMO_WEATHER_CODES = {
    0: ("Clear Sky", "Sunny / Clear weather, ideal for harvest and spraying.", "☀️"),
    1: ("Mainly Clear", "Mild sunshine with very light cloud cover.", "🌤️"),
    2: ("Partly Cloudy", "Good solar radiation for photosynthesis.", "⛅"),
    3: ("Overcast", "Cloudy sky, moderate moisture retention.", "☁️"),
    45: ("Foggy", "Low visibility and high surface dew. Watch for fungal spores.", "🌫️"),
    48: ("Depositing Rime Fog", "Dense fog; delay early morning chemical spraying.", "🌫️"),
    51: ("Light Drizzle", "Light drizzle; soil surface wetting.", "🌦️"),
    53: ("Moderate Drizzle", "Sustained drizzle; postpone fertilizer broadcasting.", "🌦️"),
    55: ("Dense Drizzle", "Wet foliage; inspect for bacterial blight.", "🌧️"),
    61: ("Slight Rain", "Light rain showers beneficial for standing crops.", "🌧️"),
    63: ("Moderate Rain", "Good soil recharge; suspend irrigation cycles.", "🌧️"),
    65: ("Heavy Rain", "High downpour; ensure drainage channels in lowlands.", "⛈️"),
    71: ("Slight Snowfall", "Cold conditions; protect nursery beds.", "🌨️"),
    80: ("Light Rain Showers", "Scattered showers; check field moisture.", "🌦️"),
    81: ("Moderate Rain Showers", "Rain showers ongoing; pause foliar spray.", "🌧️"),
    82: ("Violent Rain Showers", "High runoff risk; inspect bunds and furrows.", "⛈️"),
    95: ("Thunderstorm", "Thunderstorm alert; shelter livestock and stop field ops.", "⚡"),
    96: ("Thunderstorm with Slight Hail", "Hail hazard; inspect fruit orchards immediately.", "⛈️"),
    99: ("Thunderstorm with Heavy Hail", "Severe hail warning; post-event damage assessment advised.", "⛈️")
}

def get_weather_forecast(city_name: str = "Indore") -> dict:
    """
    Fetches real-time weather & 7-day forecast from Open-Meteo,
    plus agronomic farming advisory for temperature, humidity, and spray feasibility.
    """
    coords = LOCATIONS_DATABASE.get(city_name, LOCATIONS_DATABASE["Indore"])
    lat = coords["lat"]
    lon = coords["lon"]
    state = coords["state"]
    soil_type = coords["soil"]

    api_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m"
        "&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max"
        "&timezone=auto"
    )

    try:
        req = urllib.request.Request(api_url, headers={"User-Agent": "KisanAI/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        current = data.get("current", {})
        daily = data.get("daily", {})

        w_code = current.get("weather_code", 0)
        condition_title, condition_desc, emoji = WMO_WEATHER_CODES.get(
            w_code, ("Normal", "Fair conditions for agricultural work.", "🌤️")
        )

        temp = current.get("temperature_2m", 28.0)
        humidity = current.get("relative_humidity_2m", 55)
        wind_speed = current.get("wind_speed_10m", 10.0)
        precip = current.get("precipitation", 0.0)

        # Agronomic advisory logic
        spray_advisory = "Safe for Spraying: Wind speed and moisture are within acceptable limits."
        spray_status = "Optimal"
        if wind_speed > 18.0:
            spray_advisory = "Caution: High wind speed (>18 km/h). Spray drift may cause chemical wastage and uneven coverage."
            spray_status = "Unfavorable"
        elif humidity > 85 or precip > 0.5:
            spray_advisory = "Avoid Spraying: High moisture / precipitation will wash away chemical fungicides or pesticides."
            spray_status = "Not Recommended"

        irrigation_advisory = "Normal Scheduled Irrigation: Evapotranspiration is steady."
        if precip > 5.0:
            irrigation_advisory = "Pause Irrigation: Sufficient natural rainfall recorded."
        elif temp > 36.0 and humidity < 35:
            irrigation_advisory = "Intensify Irrigation: High heat and dry air may cause moisture stress in standing crops."

        # Format 7-day forecast
        forecast_days = []
        dates = daily.get("time", [])
        t_max = daily.get("temperature_2m_max", [])
        t_min = daily.get("temperature_2m_min", [])
        codes = daily.get("weather_code", [])
        rain_prob = daily.get("precipitation_probability_max", [])

        for i in range(min(7, len(dates))):
            c = codes[i] if i < len(codes) else 0
            cond_title, _, em = WMO_WEATHER_CODES.get(c, ("Fair", "", "🌤️"))
            forecast_days.append({
                "date": dates[i] if i < len(dates) else "",
                "temp_max": t_max[i] if i < len(t_max) else temp,
                "temp_min": t_min[i] if i < len(t_min) else temp - 8,
                "condition": cond_title,
                "icon": em,
                "rain_prob": rain_prob[i] if i < len(rain_prob) else 10
            })

        return {
            "success": True,
            "city": city_name,
            "state": state,
            "soil_type": soil_type,
            "current": {
                "temperature": temp,
                "apparent_temperature": current.get("apparent_temperature", temp),
                "humidity": humidity,
                "wind_speed": wind_speed,
                "precipitation": precip,
                "condition": condition_title,
                "description": condition_desc,
                "icon": emoji
            },
            "agri_advisory": {
                "spray_status": spray_status,
                "spray_advice": spray_advisory,
                "irrigation_advice": irrigation_advisory,
                "disease_risk": "High Fungal Risk (Humidity > 80%)" if humidity > 80 else "Normal Fungal Risk"
            },
            "daily_forecast": forecast_days
        }

    except Exception as e:
        # Graceful fallback with localized agricultural defaults
        return {
            "success": False,
            "city": city_name,
            "state": state,
            "soil_type": soil_type,
            "current": {
                "temperature": 27.5,
                "apparent_temperature": 28.0,
                "humidity": 58,
                "wind_speed": 11.2,
                "precipitation": 0.0,
                "condition": "Mainly Clear",
                "description": "Good sunlight and favorable conditions.",
                "icon": "🌤️"
            },
            "agri_advisory": {
                "spray_status": "Optimal",
                "spray_advice": "Safe for chemical/organic spraying in morning or late afternoon.",
                "irrigation_advice": "Continue standard furrow or drip irrigation schedule.",
                "disease_risk": "Normal Fungal Risk"
            },
            "daily_forecast": [
                {"date": "Day 1", "temp_max": 31, "temp_min": 19, "condition": "Sunny", "icon": "☀️", "rain_prob": 10},
                {"date": "Day 2", "temp_max": 32, "temp_min": 20, "condition": "Partly Cloudy", "icon": "⛅", "rain_prob": 15},
                {"date": "Day 3", "temp_max": 30, "temp_min": 18, "condition": "Clear", "icon": "☀️", "rain_prob": 5}
            ],
            "fallback_note": f"Real-time update fallback active: {str(e)}"
        }
