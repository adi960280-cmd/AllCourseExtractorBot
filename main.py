from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.downloader import handle_course_download
from vars import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive

keep_alive()

bot = Client("CourseExtractorBot", api_id=29115102, api_hash="1a331db2b00e9d2decaa9c7276449eb6", bot_token="8453295432:AAEgLjaT7jfNO4cl6TpW7pV-tjNIrQf2gj0")

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("""👋 Hello!

Send me a course link from:
- Classplus
- Adda247
- PW
- StudyIQ
- Utkarsh
I'll fetch PDFs, Videos & PNGs!""")

@bot.on_message(filters.text & ~filters.command(["start"]))
async def course_handler(client, message: Message):
    await handle_course_download(client, message)

bot.run()
