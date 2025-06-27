from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.downloader import handle_course_download
from keep_alive import keep_alive

keep_alive()

bot = Client("CourseExtractorBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply(
        "👋 Hello!\n\n"
        "Send me a course link from:\n"
        "- Classplus\n"
        "- Adda247\n"
        "- PW\n"
        "- StudyIQ\n"
        "- Utkarsh\n\n"
        "I'll fetch PDFs, Videos & PNGs!"
    )

@bot.on_message(filters.text & ~filters.command("start"))
def handle_course(client, message):
    handle_course_download(client, message)

bot.run()
