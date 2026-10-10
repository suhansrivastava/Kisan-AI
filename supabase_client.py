"""
KISAN AI - Supabase Client & Database Service Layer
Handles database connection, reading/inserting diagnoses, mandi rates, and chat history.
Gracefully falls back to local storage if Supabase credentials are not yet configured.
"""

import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

_supabase_client = None
_is_connected = False

def get_supabase():
    """
    Returns initialized Supabase client or None if credentials are placeholder.
    """
    global _supabase_client, _is_connected
    if _supabase_client is not None:
        return _supabase_client

    if SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL and "your-anon" not in SUPABASE_KEY:
        try:
            from supabase import create_client, Client
            _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
            _is_connected = True
            print("[KISAN AI] Supabase connected successfully to:", SUPABASE_URL)
            return _supabase_client
        except Exception as e:
            print(f"[KISAN AI] Supabase initialization warning: {e}")
            _is_connected = False
            return None
    return None

def is_supabase_configured() -> bool:
    """Checks if Supabase is connected with real credentials."""
    client = get_supabase()
    return client is not None

def save_crop_diagnosis(diagnosis_data: dict, filename: str = "") -> bool:
    """
    Persists a crop diagnosis record to the Supabase 'crop_diagnoses' table.
    """
    client = get_supabase()
    if not client:
        return False
    try:
        record = {
            "crop": diagnosis_data.get("crop", "Unknown"),
            "disease_name": diagnosis_data.get("disease_name", "Unknown"),
            "severity": diagnosis_data.get("severity", "Unknown"),
            "confidence": float(diagnosis_data.get("confidence", 0)),
            "filename": filename,
            "cause": diagnosis_data.get("cause", ""),
            "visual_metrics": diagnosis_data.get("visual_metrics", {}),
            "symptoms": diagnosis_data.get("symptoms", []),
            "chemical_treatment": diagnosis_data.get("chemical_treatment", []),
            "organic_treatment": diagnosis_data.get("organic_treatment", []),
            "prevention": diagnosis_data.get("prevention", [])
        }
        res = client.table("crop_diagnoses").insert(record).execute()
        return bool(res.data)
    except Exception as e:
        print(f"[KISAN AI] Error logging diagnosis to Supabase: {e}")
        return False

def save_chat_message(user_msg: str, bot_reply: str, lang: str = "en", bot_source: str = "Hal") -> bool:
    """
    Persists farmer chat interactions to the Supabase 'hal_chat_history' table.
    """
    client = get_supabase()
    if not client:
        return False
    try:
        record = {
            "user_message": user_msg,
            "bot_reply": bot_reply,
            "language": lang,
            "bot_source": bot_source
        }
        res = client.table("hal_chat_history").insert(record).execute()
        return bool(res.data)
    except Exception as e:
        print(f"[KISAN AI] Error logging chat to Supabase: {e}")
        return False

def fetch_mandi_rates_from_db():
    """
    Attempts to read mandi rates from Supabase table 'mandi_rates'.
    Returns list of dicts if available, otherwise None.
    """
    client = get_supabase()
    if not client:
        return None
    try:
        res = client.table("mandi_rates").select("*").execute()
        if res.data and len(res.data) > 0:
            return res.data
        return None
    except Exception as e:
        print(f"[KISAN AI] Supabase mandi rates query fallback: {e}")
        return None
