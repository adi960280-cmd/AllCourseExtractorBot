import requests

def upload_to_telegram(client, chat_id, file_url):
    file_name = file_url.split("/")[-1]
    response = requests.get(file_url)
    with open(file_name, "wb") as f:
        f.write(response.content)
    client.send_document(chat_id, document=file_name, caption="✅ File downloaded")