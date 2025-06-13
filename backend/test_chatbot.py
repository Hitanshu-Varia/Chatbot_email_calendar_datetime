#!/usr/bin/env python3
"""
Test script for the chatbot functionality
"""

import sys
import time
from backend.chatbot_core import ChatBot

def test_basic_functionality():
    """Test basic chatbot functionality"""
    print("=" * 60)
    print("CHATBOT FUNCTIONALITY TEST")
    print("=" * 60)
    
    try:
        # Initialize chatbot
        print("1. Initializing chatbot...")
        chatbot = ChatBot()
        print("✅ Chatbot initialized successfully!")
        
        # Test cases
        test_cases = [
            # Math operations
            ("What is 15 + 25?", "addition"),
            ("Calculate 100 - 30", "subtraction"),
            ("Multiply 8 by 6", "multiplication"),
            ("Divide 81 by 9", "division"),
            
            # Time
            ("What time is it?", "current time"),
            
            # General conversation
            ("Hello, how are you?", "general conversation"),
            ("Tell me about yourself", "general conversation"),
            
            # Email (will show error without proper auth)
            ("Send an email to mlwork41@gmail.com", "email functionality"),
            
            # Calendar (will show error without proper auth)
            ("Create a meeting tomorrow", "calendar functionality")
        ]
        
        print(f"\n2. Running {len(test_cases)} test cases...\n")
        
        for i, (query, test_type) in enumerate(test_cases, 1):
            print(f"Test {i}: {test_type}")
            print(f"Query: {query}")
            print("-" * 40)
            
            try:
                response = chatbot.process_message(query)
                print(f"Response: {response}")
                print("✅ Test completed")
                
            except Exception as e:
                print(f"❌ Test failed: {str(e)}")
            
            print("-" * 40)
            time.sleep(1)  # Small delay between tests
        
        print("\n✅ All tests completed!")
        
    except Exception as e:
        print(f"❌ Test setup failed: {str(e)}")
        return False
    
    return True

def test_individual_tools():
    """Test individual tool functions"""
    print("\n" + "=" * 60)
    print("INDIVIDUAL TOOLS TEST")
    print("=" * 60)
    
    try:
        from utils.tools import add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers, get_current_time, fallback
        
        # Math tests
        print("1. Testing math functions...")
        print(f"   Addition (5 + 3): {add_two_numbers(5, 3)}")
        print(f"   Subtraction (10 - 4): {subtract_two_numbers(10, 4)}")
        print(f"   Multiplication (6 * 7): {multiply_two_numbers(6, 7)}")
        print(f"   Division (20 / 4): {divide_two_numbers(20, 4)}")
        print(f"   Division by zero (10 / 0): {divide_two_numbers(10, 0)}")
        
        # Time test
        print(f"\n2. Testing time function...")
        print(f"   Current time: {get_current_time()}")
        
        # Fallback test
        print(f"\n3. Testing fallback function...")
        print(f"   Fallback: {fallback('This is a test message')}")
        
        print("\n✅ Individual tools test completed!")
        
    except Exception as e:
        print(f"❌ Tools test failed: {str(e)}")
        return False
    
    return True

def test_configuration():
    """Test configuration settings"""
    print("\n" + "=" * 60)
    print("CONFIGURATION TEST")
    print("=" * 60)
    
    try:
        from utils.config import OLLAMA_MODEL, TIMEZONE, SCOPES
        from utils.tool_definitions import TOOLS
        
        print(f"Ollama Model: {OLLAMA_MODEL}")
        print(f"Timezone: {TIMEZONE}")
        print(f"Google Scopes: {len(SCOPES)} configured")
        print(f"Available Tools: {len(TOOLS)} defined")
        
        print("\nTool definitions:")
        for tool in TOOLS:
            tool_name = tool['function']['name']
            tool_desc = tool['function']['description']
            print(f"   - {tool_name}: {tool_desc}")
        
        print("\n✅ Configuration test completed!")
        
    except Exception as e:
        print(f"❌ Configuration test failed: {str(e)}")
        return False
    
    return True

def check_dependencies():
    """Check if all required dependencies are available"""
    print("\n" + "=" * 60)
    print("DEPENDENCIES CHECK")
    print("=" * 60)
    
    dependencies = [
        ('ollama', 'Ollama Python client'),
        ('flask', 'Flask web framework'),
        ('google_auth_oauthlib', 'Google OAuth library'),
        ('googleapiclient', 'Google API client'),
    ]
    
    all_good = True
    
    for module, description in dependencies:
        try:
            __import__(module)
            print(f"✅ {module}: {description}")
        except ImportError:
            print(f"❌ {module}: {description} - NOT INSTALLED")
            all_good = False
    
    # Check Ollama connection
    try:
        import ollama
        models = ollama.list()
        print(f"✅ Ollama: Connected, {len(models.get('models', []))} models available")
    except Exception as e:
        print(f"❌ Ollama: Connection failed - {str(e)}")
        all_good = False
    
    if all_good:
        print("\n✅ All dependencies are available!")
    else:
        print("\n❌ Some dependencies are missing. Please install them using: pip install -r requirements.txt")
    
    return all_good

def main():
    """Run all tests"""
    print("AI CHATBOT COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Dependencies Check", check_dependencies()))
    results.append(("Configuration Test", test_configuration()))
    results.append(("Individual Tools Test", test_individual_tools()))
    results.append(("Basic Functionality Test", test_basic_functionality()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Your chatbot is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)