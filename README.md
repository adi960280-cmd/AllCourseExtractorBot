readme_text = """
📚 All Course Extractor Bot – by Vikash Kumar

A powerful Telegram bot that extracts and downloads videos, PDFs, and images from top e-learning platforms including:

- Classplus ✅ (working logic)
- Adda247 🕐 (coming soon)
- PW (Physics Wallah) 🕐
- StudyIQ 🕐
- Utkarsh 🕐
- Khan GS 🕐
- KD Campus 🕐
- Pathsala 🕐

🚀 Features:
- Telegram Bot Interface
- Download PDFs, Videos, and PNGs
- DRM & non-DRM support (coming soon)
- Uploads directly to Telegram
- TXT file batch link upload support
- Login and No-login both supported

🧠 Developed By:
Er. Vikash Kumar  
_Preparing for SSC JE Civil 1st Attempt_  
Built using Pyrogram, Flask, yt-dlp and more.

🔧 Deployment Guide:

Step 1: Push Code to GitHub
----------------------------
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main

Step 2: Deploy on Render
------------------------
1. Go to https://render.com
2. New > Web Service > Connect GitHub Repo
3. Set environment variables:
   - API_ID
   - API_HASH
   - BOT_TOKEN
   - CLASSPLUS_TOKEN
4. Select Python environment
5. Expose Port: 8080

🤖 Bot Commands:
- /start — Start bot
- Send course link — Bot will auto detect and extract content

📁 Folder Structure:
AllCourseExtractorBot/
│
├── main.py
├── vars.py
├── keep_alive.py
├── requirements.txt
├── render.yaml
│
├── handlers/
│   └── downloader.py
│
├── utils/
    ├── telegram_uploader.py
    └── __init__.py

📝 License:
This tool is meant for **educational purposes only**. Do not use it to distribute paid content illegally.

📞 Telegram: @Technicalboyv
❤️ Made with dedication by Vikash
"""

if __name__ == "__main__":
    print(readme_text)
