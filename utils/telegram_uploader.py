from pyrogram import Client
from pyrogram.errors import RPCError

def send_to_telegram(client: Client, chat_id: int, file_path: str, caption: str = ""):
    try:
        if file_path.endswith((".mp4", ".mkv", ".mov")):
            client.send_video(chat_id, video=file_path, caption=caption)
        elif file_path.endswith((".pdf",)):
            client.send_document(chat_id, document=file_path, caption=caption)
        elif file_path.endswith((".png", ".jpg", ".jpeg", ".webp")):
            client.send_photo(chat_id, photo=file_path, caption=caption)
        else:
            client.send_document(chat_id, document=file_path, caption=caption)
    except RPCError as e:
        client.send_message(chat_id, f"❌ Failed to upload: {str(e)}")
