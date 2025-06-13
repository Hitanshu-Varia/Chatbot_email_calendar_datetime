# Chatbot Email & Calendar Integration

## Project Overview
This project is a web-based chatbot that integrates Gmail and Google Calendar functionalities using a Python backend and a simple HTML frontend.

## Project Directory Structure
```
meow/
├── backend/
│   |
│   ├── chatbot_core.py
│   ├── run_chatbot.py
│   ├── test_chatbot.py
│   └── __init__.py
├── utils/
│   ├── config.py
│   ├── google_auth.py
│   ├── tool_definitions.py
│   └── tools.py
├── frontend/
│   ├── templates/
│   |   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
├── credentials.json
├── requirements.txt
├── .gitignore
├── app.py
├── LICENSE
└── README.md
```

### File/Directory Descriptions

- **backend/**: Contains all backend Python code for the Flask app and chatbot logic.
  - **chatbot_core.py**: Core logic for processing chatbot messages and tool calls.
  - **run_chatbot.py**: CLI entry point to interact with the chatbot in the terminal.
  - **test_chatbot.py**: Automated tests for chatbot and tool functionality.
  - **__init__.py**: Marks the backend directory as a Python package.
- **utils/**: Utility modules for configuration, authentication, and tool definitions.
  - **config.py**: Configuration settings for APIs, models, and Flask.
  - **google_auth.py**: Handles Google OAuth authentication and service creation.
  - **tool_definitions.py**: Defines available tools and their metadata for the chatbot.
  - **tools.py**: Implements tool functions (math, email, calendar, etc.).
- **frontend/**: Contains all frontend files for the web interface.
  - **templates/**: HTML templates for rendering the web UI.
    - **index.html**: Main chat interface template.
  - **static/**: Static assets (CSS, JS) for styling and interactivity.
    - **style.css**: Stylesheet for the chat interface.
    - **script.js**: JavaScript for chat functionality and UI behavior.
- **credentials.json**: Google API OAuth credentials (not committed to version control).
- **requirements.txt**: Python dependencies for the project.
- **.gitignore**: Specifies files and directories to be ignored by git.
- **LICENSE**: Project license (Apache License).
- **README.md**: Project documentation and setup instructions.
- **app.py**: Main Flask application, serves the web interface and API endpoints.

## Technology Stack
- **Backend**: Python, Flask, Ollama LLM
- **Frontend**: HTML5, CSS3, JavaScript (Jinja2)
- **Utilities**: Auth & API config, tool definitions, helper functions
- **Authentication & APIs**: Gmail API, Google Calendar API
- **Testing**: pytest

## Data Flow
1. **Frontend** (`index.html`): User interacts with the chatbot.
2. **Flask App** (`backend/app.py`): Routes requests and renders templates.
3. **Chatbot Core** (`backend/chatbot_core.py`): Handles message processing.
4. **Utilities** (`utils/`): Config, authentication handling, tools integration.
5. **Responses**: Returned to frontend as JSON or rendered HTML.

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Google Cloud Project with Calendar and Gmail APIs enabled

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Ollama

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the llama3.2 model
ollama pull llama3.2

# Start Ollama (if not running)
ollama serve
```

### 4. Google API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API and Google Calendar API
4. Create credentials (OAuth 2.0 Client ID)
5. Download the credentials file and rename it to `credentials.json`
6. Place `credentials.json` in the project root directory

### 5. Create Directory Structure

```bash
mkdir templates
# The HTML file should be placed in the templates folder
```

## Running the Application

### Option 1: Web Interface (Recommended)

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

### Option 2: Command Line Interface

```bash
python run_chatbot.py
```

### Option 3: Direct Core Testing

```bash
python chatbot_core.py
```

## Usage Examples

### Mathematics
- "What's 25 + 17?"
- "Calculate 100 - 35"
- "Multiply 8 by 7"
- "Divide 144 by 12"

### Email
- "Send an email to test@example.com with subject 'Hello' and message 'This is a test'"

### Calendar
- "Create a meeting called 'Team Standup' from 2025-06-14T10:00:00+05:30 to 2025-06-14T11:00:00+05:30"

### General
- "What time is it?"
- "Hello, how are you?"

## Configuration

Edit `config.py` to customize:

- **OLLAMA_MODEL**: Change the AI model (default: llama3.2)
- **TIMEZONE**: Set your timezone (default: Asia/Kolkata)
- **FLASK_HOST/PORT**: Modify web server settings
- **SCOPES**: Add or remove Google API permissions

## Troubleshooting

### Common Issues

1. **Ollama Connection Error**
   - Make sure Ollama is running: `ollama serve`
   - Verify the model is available: `ollama list`

2. **Google Authentication Error**
   - Check if `credentials.json` exists and is valid
   - Ensure APIs are enabled in Google Cloud Console
   - Try deleting and recreating OAuth credentials

3. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

4. **Flask Server Issues**
   - Check if port 5000 is available
   - Try changing the port in `config.py`

### Debug Mode

Enable debug logging by setting `FLASK_DEBUG = True` in `config.py`.

## API Endpoints

- `GET /` - Main chat interface
- `POST /chat` - Send message to chatbot
- `GET /status` - Check chatbot status
- `GET /health` - Health check

## Security Notes

- Keep your `credentials.json` file secure and never commit it to version control
- The application runs locally by default - configure properly for production use
- Consider implementing rate limiting for production deployments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the Apache License.

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are properly installed
3. Verify your Google API setup
4. Check the console output for detailed error messages

---

**Note**: This chatbot requires active internet connection for Google API calls and Ollama model interactions.
