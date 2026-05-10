from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/documents"]

flow = InstalledAppFlow.from_client_secrets_file("oauth_credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

service = build("docs", "v1", credentials=creds)

document = service.documents().create(body={"title": "Pythonから作成したドキュメント"}).execute()
doc_id = document["documentId"]

print("ドキュメント作成完了！")
print("ドキュメントID:", doc_id)

requests = [
    {
        "insertText": {
            "location": {"index": 1},
            "text": "こんにちは！PythonからGoogle Docsに書き込みました！"
        }
    }
]

service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

print("テキスト挿入完了！")
print("URL: https://docs.google.com/document/d/" + doc_id)