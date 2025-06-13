from flask import Flask, render_template, request, jsonify
from backend.chatbot_core import ChatBot
from utils.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
import threading
import time

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

# Initialize chatbot
chatbot = None
chatbot_ready = False

def initialize_chatbot():
    """Initialize chatbot in a separate thread"""
    global chatbot, chatbot_ready
    try:
        chatbot = ChatBot()
        chatbot_ready = True
        print("Chatbot initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize chatbot: {str(e)}")
        chatbot_ready = False

# Initialize chatbot in background
threading.Thread(target=initialize_chatbot, daemon=True).start()

@app.route('/')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        # Check if chatbot is ready
        if not chatbot_ready or chatbot is None:
            return jsonify({
                'success': False,
                'response': 'Chatbot is still initializing. Please wait a moment and try again.'
            })
        
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'response': 'Please enter a message.'
            })
        
        # Process message with chatbot
        bot_response = chatbot.process_message(user_message)
        
        return jsonify({
            'success': True,
            'response': bot_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'response': f'Sorry, I encountered an error: {str(e)}'
        })

@app.route('/status')
def status():
    """Check chatbot status"""
    return jsonify({
        'ready': chatbot_ready,
        'status': 'ready' if chatbot_ready else 'initializing'
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'chatbot_ready': chatbot_ready
    })

if __name__ == '__main__':
    print("Starting Flask application...")
    print(f"Open your browser and go to: http://{FLASK_HOST}:{FLASK_PORT}")
    
    # Wait a bit for chatbot to initialize
    time.sleep(2)
    
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG
    )
