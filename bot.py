import os
import requests

TOKEN = os.getenv("7989720535:AAHD4aFO_LaQiE9cltj9Uk4HcMRUeMa5Bas")
CHAT_ID = "833132332"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

send_message("🚀 Bot activo. Sistema iniciado correctamente.")
