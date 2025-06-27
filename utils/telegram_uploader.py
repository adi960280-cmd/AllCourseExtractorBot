from pyrogram import Client
from pyrogram.types import Message

def send_to_telegram(client: Client, chat_id: int, file_path: str, caption: str = ""):
    client.send_document(chat_id=chat_id, document=file_path, caption=caption)
