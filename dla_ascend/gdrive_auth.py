"""
One-time OAuth flow to get a Google Drive token with write scope.
Run: python3 dla_ascend/gdrive_auth.py
Then open the URL it prints, authorize, and paste back the code.
"""
import json
import urllib.parse
import urllib.request
import http.server
import threading
import webbrowser
import os

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
REDIRECT_URI = "http://localhost:3000/oauth2callback"
TOKEN_PATH = os.path.expanduser("~/.config/mcp-gdrive/gdrive-token.json")

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/presentations",
]

auth_code = None

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<h2>Authorization successful! You can close this tab.</h2>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"No code received.")

    def log_message(self, *args):
        pass  # Suppress server logs

def get_token(code):
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def main():
    params = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
    })
    auth_url = f"https://accounts.google.com/o/oauth2/auth?{params}"

    print("\n" + "="*60)
    print("Opening browser for Google Drive authorization...")
    print("If browser doesn't open, visit this URL manually:")
    print(f"\n{auth_url}\n")
    print("="*60 + "\n")

    # Start local callback server
    server = http.server.HTTPServer(("localhost", 3000), CallbackHandler)
    server_thread = threading.Thread(target=server.handle_request)
    server_thread.daemon = True
    server_thread.start()

    webbrowser.open(auth_url)
    server_thread.join(timeout=120)

    if not auth_code:
        print("No authorization code received. Did you complete the browser flow?")
        return

    print("Code received. Exchanging for token...")
    token = get_token(auth_code)

    os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
    with open(TOKEN_PATH, "w") as f:
        json.dump(token, f, indent=2)

    print(f"\nToken saved to: {TOKEN_PATH}")
    print(f"Scopes granted: {token.get('scope', 'unknown')}")
    print(f"Refresh token: {'YES' if 'refresh_token' in token else 'NO'}")
    print("\nDrive write access is ready!")

if __name__ == "__main__":
    main()
