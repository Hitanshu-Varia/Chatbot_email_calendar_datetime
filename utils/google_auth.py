from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from utils.config import SCOPES, CREDENTIALS_FILE

class GoogleAuth:
    def __init__(self):
        self.credentials = None
        self.calendar_service = None
        self.gmail_service = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google APIs"""
        try:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(f"Credentials file '{CREDENTIALS_FILE}' not found")
            
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            self.credentials = flow.run_local_server(port=0)
            
            # Build services
            self.calendar_service = build("calendar", "v3", credentials=self.credentials)
            self.gmail_service = build("gmail", "v1", credentials=self.credentials)
            
            print("Google authentication successful!")
            
        except Exception as e:
            print(f"Authentication failed: {str(e)}")
            raise
    
    def get_calendar_service(self):
        return self.calendar_service
    
    def get_gmail_service(self):
        return self.gmail_service

# Global authentication instance
auth_instance = None

def get_auth_instance():
    global auth_instance
    if auth_instance is None:
        auth_instance = GoogleAuth()
    return auth_instance