import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests

# Load API key
load_dotenv()
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

app = Flask(__name__)

def get_bot_response(user_input):
    """Call Gemini API for chatbot response with error handling"""
    headers = {
        "Content-Type": "application/json",
    }
    params = {
        "key": GOOGLE_GENAI_API_KEY
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)
        print("Status code:", response.status_code)
        print("Response body:", response.text)

        response.raise_for_status()
        data = response.json()

        # Gemini returns candidates → content → parts → text
        return (
            data.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "No response from Gemini.")
        )
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.status_code == 401:
            return "API key unauthorized. Check your Google key."
        elif response.status_code == 403:
            return "Access forbidden. Check API access permissions."
        else:
            return f"HTTP error: {response.status_code}"
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return "Network error or API is unreachable."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_reply():
    user_msg = request.json.get("message", "")
    if not user_msg.strip():
        return jsonify({"reply": "Please type a message."})
    bot_reply = get_bot_response(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
