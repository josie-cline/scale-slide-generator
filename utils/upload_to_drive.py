"""
Uploads ASCEND_PoC_Plan_OP2.docx to Google Drive, converting to Google Doc.
Run: python3 dla_ascend/upload_to_drive.py
"""
import json, os, urllib.request, urllib.parse

TOKEN_PATH = os.path.expanduser("~/.config/mcp-gdrive/gdrive-token.json")
CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
FILE_PATH = "dla_ascend/ASCEND_PoC_Plan_OP2.docx"
FILE_NAME = "ASCEND PoC Plan - Option Period 2"

def refresh_access_token(refresh_token):
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["access_token"]

def upload_file(access_token, file_path, file_name):
    with open(file_path, "rb") as f:
        file_data = f.read()

    boundary = "boundary_ascend_upload"
    metadata = json.dumps({
        "name": file_name,
        "mimeType": "application/vnd.google-apps.document",
    }).encode()

    body = (
        f"--{boundary}\r\n"
        f"Content-Type: application/json; charset=UTF-8\r\n\r\n"
    ).encode() + metadata + (
        f"\r\n--{boundary}\r\n"
        f"Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--".encode()

    req = urllib.request.Request(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,webViewLink",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": f"multipart/related; boundary={boundary}",
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def main():
    with open(TOKEN_PATH) as f:
        token_data = json.load(f)

    access_token = refresh_access_token(token_data["refresh_token"])
    print(f"Uploading '{FILE_NAME}' to Google Drive...")
    result = upload_file(access_token, FILE_PATH, FILE_NAME)
    print(f"\nUpload successful!")
    print(f"File ID:  {result['id']}")
    print(f"URL:      {result['webViewLink']}")

if __name__ == "__main__":
    main()
