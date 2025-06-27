import re
from pyrogram.types import Message
from utils.telegram_uploader import send_to_telegram
def send_mock_file(client, message, platform):
    try:
        dummy_file = "your_existing_video.mp4"  # ensure file is present in repo
        caption = f"🎬 Sample lecture from {platform}"
        send_to_telegram(client, message.chat.id, dummy_file, caption)
    except Exception as e:
        message.reply(f"❌ Error sending file: {str(e)}")

def handle_course_download(client, message: Message):
    text = message.text.strip().lower()

    if "/start" in text:
        message.reply(
            "👋 Hello!\n\nSend me a course link from:\n- Classplus\n- Adda247\n- PW\n- StudyIQ\n- Utkarsh\n- Khan GS\n- KD Campus\n- Pathsala\n\nI'll fetch PDFs, Videos & PNGs!"
        )
        return

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
        message.reply("❌ Unsupported or unrecognized course platform. Please send a valid course link from the supported platforms.")


def handle_classplus(client, message, url):
    message.reply("🎯 Processing Classplus course link...")
    course_id = extract_id(url)
    message.reply(f"✅ Course ID: {course_id} (Classplus)")
    send_mock_file(client, message, "Classplus")


def handle_adda247(client, message, url):
    message.reply("🎯 Processing Adda247 course link...")
    send_mock_file(client, message, "Adda247")


def handle_studyiq(client, message, url):
    message.reply("🎯 Processing StudyIQ course link...")
    send_mock_file(client, message, "StudyIQ")


def handle_utkarsh(client, message, url):
    message.reply("🎯 Processing Utkarsh course link...")
    send_mock_file(client, message, "Utkarsh")


def handle_khangs(client, message, url):
    message.reply("🎯 Processing Khan GS course link...")
    send_mock_file(client, message, "Khan GS")


def handle_pw(client, message, url):
    message.reply("🎯 Processing Physics Wallah course link...")
    send_mock_file(client, message, "Physics Wallah")


def handle_kdcampus(client, message, url):
    message.reply("🎯 Processing KD Campus course link...")
    send_mock_file(client, message, "KD Campus")


def handle_pathsala(client, message, url):
    message.reply("🎯 Processing Pathsala course link...")
    send_mock_file(client, message, "Pathsala")


def send_mock_file(client, message, platform):
    try:
        dummy_file = "sample_video.mp4"  # Placeholder file
        caption = f"🎬 Sample lecture from {platform} (Mock file only)"
        send_to_telegram(client, message.chat.id, dummy_file, caption)
    except Exception as e:
        message.reply(f"❌ Error sending file: {str(e)}")


def extract_id(url):
    match = re.search(r'/course-detail/([a-zA-Z0-9]+)', url)
    return match.group(1) if match else "unknown"
    
