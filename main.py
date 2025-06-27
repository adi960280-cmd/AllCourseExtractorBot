from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.downloader import handle_course_download
from vars import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive

keep_alive()

bot = Client("CourseExtractorBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("👋 Hello!

Send me a course link from:
- Classplus
- Adda247
- PW
- StudyIQ
- Utkarsh
I'll fetch PDFs, Videos & PNGs!")

@bot.on_message(filters.text & ~filters.command(["start"]))
async def course_handler(client, message: Message):
    await handle_course_download(client, message)

bot.run()
