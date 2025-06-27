from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive
from handlers.downloader import handle_course_download

keep_alive()
bot = Client("course_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply(
        "👋 Hello!\n\nSend me a course link from:\n- Classplus\n- Adda247\n- PW\n- StudyIQ\n- Utkarsh\nI'll fetch PDFs, Videos & PNGs!"
    )

@bot.on_message(filters.text & ~filters.command(["start"]))
def get_course(client, message):
    handle_course_download(client, message)

bot.run()