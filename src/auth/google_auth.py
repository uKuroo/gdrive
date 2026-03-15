import os
import json
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from google.oauth2 import service_account

from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
AUTH_DIR = Path(__file__).resolve().parent / 'credentials'

def authenticate_oauth(client_secret_file: Path) -> object:
    token_file = client_secret_file.parent / 'token.json'
    creds = None

    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(client_secret_file), SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    return creds

def authenticate_service_account(client_secret_file: Path) -> object:
    creds = service_account.Credentials.from_service_account_file(
        str(client_secret_file), scopes=SCOPES
    )
    return creds

def authenticate_drive() -> object:
    auth_dir = AUTH_DIR
    credentials_file = auth_dir / 'credentials.json'

    if not credentials_file.exists():
        raise FileNotFoundError(
            f"Credentials not found at: {credentials_file}\n"
            "Please add your 'credentials.json' (OAuth or Service Account) to the directory."
        )

    with open(credentials_file, 'r') as f:
        try:
            cred_data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("credentials.json is not a valid JSON file.")

    if cred_data.get('type') == 'service_account':
        creds = authenticate_service_account(credentials_file)
    elif 'installed' in cred_data or 'web' in cred_data:
        creds = authenticate_oauth(credentials_file)
    else:
        raise ValueError(
            "Unrecognized credentials format. The JSON must be either "
            "a Service Account key or an OAuth 2.0 Client ID."
        )

    return build('drive', 'v3', credentials=creds)