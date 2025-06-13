import os

# Google API Configuration
SCOPES = [
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/gmail.send"
]

# Credentials file path
CREDENTIALS_FILE = "credentials.json"

# Ollama Configuration
OLLAMA_MODEL = "llama3.2"

# Timezone
TIMEZONE = "Asia/Kolkata"

# Flask Configuration
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
FLASK_DEBUG = True