from email.mime.text import MIMEText
import base64
import datetime
from utils.google_auth import get_auth_instance
from utils.config import TIMEZONE

def send_email(to: str, subject: str, message: str) -> str:
    """Send an email using Gmail API"""
    try:
        print(f"Sending email to {to}...")
        
        auth = get_auth_instance()
        gmail_service = auth.get_gmail_service()
        
        mime_message = MIMEText(message)
        mime_message["to"] = to
        mime_message["subject"] = subject
        raw = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

        message_body = {"raw": raw}
        sent_message = gmail_service.users().messages().send(
            userId="me", body=message_body
        ).execute()
        
        result = f"✅ Email sent successfully to {to} with ID: {sent_message['id']}"
        print(result)
        return result
        
    except Exception as e:
        error_msg = f"❌ Failed to send email: {str(e)}"
        print(error_msg)
        return error_msg

def create_calendar_event(summary: str, start_time: str, end_time: str) -> str:
    """Create an event in Google Calendar"""
    try:
        print(f"Creating calendar event: {summary}")
        
        auth = get_auth_instance()
        calendar_service = auth.get_calendar_service()
        
        event = {
            "summary": summary,
            "start": {"dateTime": start_time, "timeZone": TIMEZONE},
            "end": {"dateTime": end_time, "timeZone": TIMEZONE},
        }
        
        event_result = calendar_service.events().insert(
            calendarId="primary", body=event
        ).execute()
        
        result = f"✅ Calendar event '{summary}' created successfully: {event_result.get('htmlLink')}"
        print(result)
        return result
        
    except Exception as e:
        error_msg = f"❌ Failed to create calendar event: {str(e)}"
        print(error_msg)
        return error_msg

def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    try:
        print(f"Adding {a} + {b}")
        result = int(a) + int(b)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error in addition: {str(e)}")
        return 0

def subtract_two_numbers(a: int, b: int) -> int:
    """Subtract two numbers"""
    try:
        print(f"Subtracting {a} - {b}")
        result = int(a) - int(b)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error in subtraction: {str(e)}")
        return 0

def multiply_two_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    try:
        print(f"Multiplying {a} * {b}")
        result = int(a) * int(b)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error in multiplication: {str(e)}")
        return 0

def divide_two_numbers(a: int, b: int) -> float:
    """Divide two numbers"""
    try:
        print(f"Dividing {a} / {b}")
        if int(b) == 0:
            return "❌ Cannot divide by zero"
        result = int(a) / int(b)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error in division: {str(e)}")
        return 0

def get_current_time() -> str:
    """Get current date and time"""
    try:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        result = f"Current date and time: {formatted_time}"
        print(result)
        return result
    except Exception as e:
        error_msg = f"Error getting current time: {str(e)}"
        print(error_msg)
        return error_msg

def fallback(message: str) -> str:
    """Fallback function for general responses"""
    print("Using fallback function for general response")
    return f"I understand you said: {message}. I'm a chatbot that can help with calculations, sending emails, creating calendar events, and answering questions. How can I assist you today?"

# Available functions registry
AVAILABLE_FUNCTIONS = {
    'add_two_numbers': add_two_numbers,
    'subtract_two_numbers': subtract_two_numbers,
    'multiply_two_numbers': multiply_two_numbers,
    'divide_two_numbers': divide_two_numbers,
    'create_calendar_event': create_calendar_event,
    'send_email': send_email,
    'get_current_time': get_current_time,
    'fallback': fallback
}