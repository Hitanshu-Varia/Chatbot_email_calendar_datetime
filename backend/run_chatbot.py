#!/usr/bin/env python3
"""
Standalone chatbot runner for testing without the web interface
"""

from backend.chatbot_core import ChatBot
import sys

def main():
    """Main function to run the chatbot"""
    print("=" * 50)
    print("AI CHATBOT - STANDALONE MODE")
    print("=" * 50)
    
    try:
        # Initialize chatbot
        print("Initializing chatbot...")
        chatbot = ChatBot()
        print("Chatbot initialized successfully!")
        
        # Start interactive chat
        chatbot.chat_interactive()
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
        print("Please make sure:")
        print("1. Ollama is installed and running")
        print("2. The llama3.2 model is downloaded")
        print("3. Your credentials.json file is properly configured")
        sys.exit(1)

if __name__ == "__main__":
    main()