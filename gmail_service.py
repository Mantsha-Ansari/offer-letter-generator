import os
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# Gmail API ke liye credentials.json ka path
CREDENTIALS_FILE = "credentials.json"

# Gmail API service initialize karo
def gmail_authenticate():
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=["https://www.googleapis.com/auth/gmail.send"]
    )
    service = build("gmail", "v1", credentials=credentials)
    return service

# Email send karne ka function
def send_email(to, subject, body):
    service = gmail_authenticate()
    
    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
    try:
        send_message = service.users().messages().send(
            userId="me",
            body={"raw": raw}
        ).execute()
        return send_message
    except Exception as e:
        return f"❌ Error: {e}"
