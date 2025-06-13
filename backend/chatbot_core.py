from ollama import chat, ChatResponse
from utils.tools import AVAILABLE_FUNCTIONS
from utils.tool_definitions import TOOLS
from utils.config import OLLAMA_MODEL
import json

class ChatBot:
    def __init__(self):
        self.model = OLLAMA_MODEL
        self.tools = TOOLS
        self.available_functions = AVAILABLE_FUNCTIONS
        print(f"ChatBot initialized with model: {self.model}")
    
    def process_message(self, user_message: str) -> str:
        """Process user message and return response"""
        try:
            print(f"\n--- Processing message: {user_message} ---")
            
            # Get response from Ollama
            response: ChatResponse = chat(
                self.model,
                messages=[
                    {
                        'role': 'user',
                        'content': user_message
                    }
                ],
                tools=self.tools,
            )
            
            # Initialize response parts
            response_parts = []
            
            # Add the main response content if available
            if hasattr(response.message, 'content') and response.message.content:
                response_parts.append(response.message.content)
            
            # Process tool calls if any
            if hasattr(response.message, 'tool_calls') and response.message.tool_calls:
                print(f"Found {len(response.message.tool_calls)} tool call(s)")
                
                for tool in response.message.tool_calls:
                    function_name = tool.function.name
                    function_args = tool.function.arguments
                    
                    print(f"Calling function: {function_name}")
                    print(f"Arguments: {function_args}")
                    
                    if function_to_call := self.available_functions.get(function_name):
                        try:
                            # Call the function with the arguments
                            function_result = function_to_call(**function_args)
                            
                            # Format the result
                            if isinstance(function_result, (int, float)):
                                result_text = f"Result: {function_result}"
                            else:
                                result_text = str(function_result)
                            
                            response_parts.append(result_text)
                            print(f"Function output: {result_text}")
                            
                        except Exception as e:
                            error_msg = f"Error executing {function_name}: {str(e)}"
                            response_parts.append(error_msg)
                            print(error_msg)
                    else:
                        error_msg = f"Function '{function_name}' not found"
                        response_parts.append(error_msg)
                        print(error_msg)
            else:
                # No tool calls, use fallback for general conversation
                if not response_parts:
                    fallback_result = self.available_functions['fallback'](user_message)
                    response_parts.append(fallback_result)
            
            # Combine all response parts
            final_response = "\n\n".join(response_parts) if response_parts else "I'm not sure how to respond to that."
            
            print(f"Final response: {final_response}")
            return final_response
            
        except Exception as e:
            error_response = f"Sorry, I encountered an error: {str(e)}"
            print(f"Error in process_message: {error_response}")
            return error_response
    
    def chat_interactive(self):
        """Interactive chat mode for testing"""
        print("ChatBot is ready! Type 'quit' to exit.")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                response = self.process_message(user_input)
                print(f"\nBot: {response}")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")

# For testing purposes
if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat_interactive()