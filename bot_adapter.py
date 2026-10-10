"""
========================================================================================
KISAN AI - BOT INTEGRATION ADAPTER / HOOK
========================================================================================
This file is specially dedicated for linking your friend's chatbot code or external AI service!

You can link your friend's code in ANY of the following ways:

Option 1: Python function import
    If your friend wrote a Python file (e.g., `friends_bot.py`), import their function:
    ```python
    from friends_bot import generate_response
    # then call generate_response(user_message, language) inside custom_friend_bot()
    ```

Option 2: REST API / Webhook (FastAPI, Flask, Node.js, LangChain, etc.)
    If your friend is running a local or remote server (e.g. http://localhost:8000/chat),
    simply set `FRIEND_BOT_API_URL` below and set `USE_FRIEND_BOT = True`.

Option 3: Directly write or paste your friend's code inside `custom_friend_bot()` below!
========================================================================================
"""

import urllib.request
import json

# Set this to True once you want KISAN AI to use your friend's bot instead of the built-in Hal logic
USE_FRIEND_BOT = False

# If your friend runs an API server (e.g. FastAPI, Node, Ollama, LangChain server), put the URL here:
FRIEND_BOT_API_URL = "http://localhost:8000/api/chat"


def custom_friend_bot(message: str, lang: str = "en") -> dict:
    """
    ==============================================================================
    👉 PLACE YOUR FRIEND'S CODE HERE OR CALL THEIR FUNCTION / API
    ==============================================================================
    Arguments:
        message (str): The question asked by the farmer (e.g. "What is today's wheat price?")
        lang (str): Selected language code ('hi', 'en', 'pa', 'te', 'ta', 'bn')

    Return format expected by KISAN AI frontend:
    {
        "success": True,
        "bot_name": "Hal (Powered by Friend's Model)",
        "reply": "Your response string here (supports text or HTML)",
        "suggestions": ["Optional quick follow-up question 1", "Question 2"]
    }
    """

    # --- EXAMPLE IMPLEMENTATION A: Calling your friend's REST API ---
    if FRIEND_BOT_API_URL and USE_FRIEND_BOT:
        try:
            payload = json.dumps({"query": message, "language": lang}).encode("utf-8")
            req = urllib.request.Request(
                FRIEND_BOT_API_URL,
                data=payload,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                # Adapt your friend's response format if needed:
                return {
                    "success": True,
                    "bot_name": data.get("bot_name", "Hal (Friend AI)"),
                    "reply": data.get("reply") or data.get("response") or str(data),
                    "suggestions": data.get("suggestions", ["Mandi Rates", "Crop Disease", "Weather Forecast"])
                }
        except Exception as e:
            return {
                "success": True,
                "bot_name": "Hal (Friend Bot Bridge)",
                "reply": f"⚠️ Notice: Connected to friend's bot hook, but endpoint returned: {str(e)}. Please check if your friend's bot server is running.",
                "suggestions": ["Check Server", "Mandi Rates", "Crop Disease"]
            }

    # --- EXAMPLE IMPLEMENTATION B: If your friend gives you a Python script ---
    # Example:
    # try:
    #     import friend_model
    #     reply_text = friend_model.predict(message)
    #     return {"success": True, "bot_name": "Hal (Custom)", "reply": reply_text, "suggestions": []}
    # except ImportError:
    #     pass

    # Default fallback placeholder when USE_FRIEND_BOT is False
    return {
        "success": False,
        "message": "Friend bot hook is currently disabled. Set USE_FRIEND_BOT = True in bot_adapter.py."
    }
