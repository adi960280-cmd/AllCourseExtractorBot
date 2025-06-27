from utils.classplus import process_classplus
from utils.adda247 import process_adda247
from utils.pw import process_pw
from utils.studyiq import process_studyiq

def handle_course_download(client, message):
    url = message.text.strip()
    message.reply("🔍 Processing your course link...")

    if "classplusapp.com" in url:
        process_classplus(client, message, url)
    elif "adda247.com" in url:
        process_adda247(client, message, url)
    elif "study" in url:
        process_studyiq(client, message, url)
    elif "pw.live" in url or "pwskills" in url:
        process_pw(client, message, url)
    else:
        message.reply("❌ Unsupported or unrecognized link.")