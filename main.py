# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     All Course Extractor - Vikash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from vars import API_ID, API_HASH, BOT_TOKEN
from keep_alive import keep_alive
from handlers.downloader import handle_course_download

# Start the keep-alive server (Render Port 8080 Support)
keep_alive()

# Create the bot client
bot = Client("AllCourseExtractorBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# /start command handler
@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text(
        "**👋 Hello!**\n\n"
        "I'm your Course Extractor Bot 🤖\n\n"
        "📥 Send me any valid course link from:\n"
        "- Classplus\n"
        "- Adda247\n"
        "- PW (Physics Wallah)\n"
        "- StudyIQ\n"
        "- Utkarsh\n"
        "- Khan GS\n"
        "- KD Campus\n"
        "- Pathsala\n\n"
        "I'll extract & send you videos, PDFs, or images 📚🎥📄\n\n"
        "Made by **Vikash Kumar**"
    )

# Handle any text message as course URL
@bot.on_message(filters.text & ~filters.command(["start"]))
async def handle_course(client: Client, message: Message):
    await message.reply("🔍 Processing your course link... Please wait ⏳")
    await handle_course_download(client, message)

# Run the bot
bot.run()
