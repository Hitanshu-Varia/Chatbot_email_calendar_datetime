const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const typingIndicator = document.getElementById('typingIndicator');

// Check chatbot status on load
async function checkStatus() {
    try {
        const response = await fetch('/status');
        const data = await response.json();
        if (!data.ready) {
            addMessage('bot', 'I\'m still initializing. Please wait a moment...');
            setTimeout(checkStatus, 2000);
        }
    } catch (error) {
        console.error('Status check failed:', error);
    }
}

function addMessage(sender, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = sender === 'user' ? '👤' : '🤖';
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = content;
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(messageContent);
    // Remove welcome message if it exists
    const welcomeMessage = chatMessages.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTyping() {
    typingIndicator.style.display = 'flex';
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function hideTyping() {
    typingIndicator.style.display = 'none';
}

async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;
    addMessage('user', message);
    messageInput.value = '';
    sendButton.disabled = true;
    sendButton.textContent = 'Sending...';
    showTyping();
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        const data = await response.json();
        hideTyping();
        if (data.success) {
            addMessage('bot', data.response);
        } else {
            addMessage('bot', data.response || 'Sorry, I encountered an error.');
        }
    } catch (error) {
        hideTyping();
        addMessage('bot', 'Sorry, I couldn\'t process your request. Please check your connection and try again.');
        console.error('Error:', error);
    } finally {
        sendButton.disabled = false;
        sendButton.textContent = 'Send';
    }
}

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
messageInput.focus();
checkStatus();
setTimeout(() => {
    if (chatMessages.querySelector('.welcome-message')) {
        const examples = [
            "Try asking me: 'What's 25 + 17?'",
            "Or: 'Send an email to test@example.com'",
            "Or: 'Create a meeting for tomorrow at 2 PM'",
            "Or: 'What time is it?'"
        ];
        examples.forEach((example, index) => {
            setTimeout(() => {
                const exampleDiv = document.createElement('div');
                exampleDiv.style.cssText = `
                    background: #e3f2fd;
                    border: 1px solid #bbdefb;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px 0;
                    font-size: 0.9rem;
                    color: #1976d2;
                    cursor: pointer;
                    transition: all 0.2s ease;
                `;
                exampleDiv.textContent = example;
                exampleDiv.addEventListener('click', () => {
                    messageInput.value = example.replace("Try asking me: '", "").replace("Or: '", "").replace("'", "");
                    messageInput.focus();
                });
                exampleDiv.addEventListener('mouseenter', () => {
                    exampleDiv.style.backgroundColor = '#bbdefb';
                });
                exampleDiv.addEventListener('mouseleave', () => {
                    exampleDiv.style.backgroundColor = '#e3f2fd';
                });
                const welcomeMessage = chatMessages.querySelector('.welcome-message');
                if (welcomeMessage) {
                    welcomeMessage.appendChild(exampleDiv);
                }
            }, index * 500);
        });
    }
}, 1000);
