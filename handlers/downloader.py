import re
import json
import requests
from pyrogram.types import Message
from utils.telegram_uploader import send_to_telegram


def handle_course_download(client, message: Message):
    text = message.text.strip().lower()

    platforms = {
        "classplus": handle_classplus,
        "adda247": handle_adda247,
        "studyiq": handle_studyiq,
        "utkarsh": handle_utkarsh,
        "khangs": handle_khangs,
        "khangsclasses": handle_khangs,
        "pw.live": handle_pw,
        "pwskills": handle_pw,
        "kdclasses": handle_kdcampus,
        "kdcampus": handle_kdcampus,
        "pathsala": handle_pathsala,
    }

    matched = False
    for key in platforms:
        if key in text:
            platforms[key](client, message, text)
            matched = True
            break

    if not matched:
        message.reply("❌ Unsupported or unrecognized course platform.")


# Real Classplus Extractor Logic

def handle_classplus(client, message, url):
    message.reply("🎯 Processing Classplus course link...")
    course_id = extract_id(url)
    message.reply(f"✅ Course ID: {course_id} (Classplus)")

    try:
        token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9...your-token"
        headers = {
            "x-access-token": token,
            "Content-Type": "application/json"
        }

        response = requests.get(
            f"https://api.classplusapp.com/cams/api/student/course/{course_id}/details",
            headers=headers
        )

        if response.status_code != 200:
            message.reply("❌ Failed to fetch course data.")
            return

        data = response.json()
        course_title = data.get("data", {}).get("course", {}).get("title", "Course")
        items = data.get("data", {}).get("course", {}).get("chapters", [])

        for chapter in items:
            for content in chapter.get("contents", []):
                content_type = content.get("type")
                title = content.get("name")
                url = content.get("url")

                if content_type == 1:
                    filename = f"{course_title}_{title}.mp4"
                elif content_type == 2:
                    filename = f"{course_title}_{title}.pdf"
                elif content_type == 3:
                    filename = f"{course_title}_{title}.png"
                else:
                    continue

                send_to_telegram(client, message.chat.id, url, filename)

        message.reply("✅ Done sending course materials.")

    except Exception as e:
        message.reply(f"❌ Error: {str(e)}")


def handle_adda247(client, message, url):
    message.reply("🎯 Processing Adda247 course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ Adda247 logic not yet implemented.")


def handle_studyiq(client, message, url):
    message.reply("🎯 Processing StudyIQ course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ StudyIQ logic not yet implemented.")


def handle_utkarsh(client, message, url):
    message.reply("🎯 Processing Utkarsh course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ Utkarsh logic not yet implemented.")


def handle_khangs(client, message, url):
    message.reply("🎯 Processing Khan GS course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ Khan GS logic not yet implemented.")


def handle_pw(client, message, url):
    message.reply("🎯 Processing Physics Wallah course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ PW logic not yet implemented.")


def handle_kdcampus(client, message, url):
    message.reply("🎯 Processing KD Campus course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ KD Campus logic not yet implemented.")


def handle_pathsala(client, message, url):
    message.reply("🎯 Processing Pathsala course link... (Extracting content)")
    # Placeholder logic — update when API/URL known
    message.reply("❌ Pathsala logic not yet implemented.")


def extract_id(url):
    match = re.search(r'/course-detail/([a-zA-Z0-9]+)', url)
    return match.group(1) if match else "unknown"
    
