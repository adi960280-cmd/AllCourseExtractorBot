import re
import requests
from pyrogram.types import Message
from utils.telegram_uploader import send_to_telegram

def handle_course_download(client, message: Message):
    text = message.text.strip().lower()
    if "classplus" in text:
        handle_classplus(client, message, text)
    else:
        message.reply("❌ Unsupported or unrecognized course platform.")

def handle_classplus(client, message, url):
    message.reply("🎯 Processing Classplus course link...")
    course_id = extract_id(url)
    message.reply(f"✅ Course ID: {course_id} (Classplus)")
    try:
        token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6OTg5OTAxMzcs..."
        headers = {
            "x-access-token": token,
            "Content-Type": "application/json"
        }
        res = requests.get(f"https://api.classplusapp.com/cams/api/student/course/{course_id}/details", headers=headers)
        if res.status_code != 200:
            message.reply("❌ Failed to fetch course data.")
            return
        course = res.json().get("data", {}).get("course", {})
        for chapter in course.get("chapters", []):
            for content in chapter.get("contents", []):
                title = content.get("name", "file")
                url = content.get("url", "")
                ext = ".mp4" if content.get("type") == 1 else ".pdf" if content.get("type") == 2 else ".png"
                filename = f"{course.get('title')}_{title}{ext}"
                send_to_telegram(client, message.chat.id, url, filename)
        message.reply("✅ Course content sent.")
    except Exception as e:
        message.reply(f"❌ Error: {str(e)}")

def extract_id(url):
    match = re.search(r'/course-detail/([a-zA-Z0-9]+)', url)
    return match.group(1) if match else "unknown"
