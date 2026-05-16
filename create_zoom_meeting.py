import requests
import json
import os
from base64 import b64encode
from dotenv import load_dotenv

load_dotenv()
ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")

def get_access_token():
    credentials = b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={ACCOUNT_ID}"
    headers = {"Authorization": f"Basic {credentials}"}
    response = requests.post(url, headers=headers)
    return response.json()["access_token"]

def create_meeting(token):
    url = "https://api.zoom.us/v2/users/me/meetings"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    body = {
        "topic": "テスト会議",
        "type": 2,
        "settings": {"password": "123456"}
ers=headers, json=body)
    return response.json()

def main():
    token = get_access_token()
    meeting = create_meeting(token)
    print("✅ Zoomミーティングを作成しました！")
    print(f"📋 ミーティングID: {meeting['id']}")
    print(f"🔑 パスワード: {meeting['password']}")
    print(f"🔗 参加リンク: {meeting['join_url']}")

if __name__ == "__main__":
    main()
