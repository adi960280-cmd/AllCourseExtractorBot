import requests
from pyrogram import Client

def send_to_telegram(client: Client, chat_id: int, url: str, filename: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        client.send_document(chat_id, document=filename, caption=filename)
