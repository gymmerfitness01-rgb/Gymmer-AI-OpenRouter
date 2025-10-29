"""
Simple test script to verify OpenRouter API connection.
This helps you test if your API key and model are working.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv('OPENROUTER_API_KEY')

if not api_key:
    print("❌ ERROR: OPENROUTER_API_KEY not found in environment variables!")
    print("Make sure you have a .env file with your API key set.")
    exit(1)

print(f"✅ API Key found: {api_key[:20]}...")

# Initialize OpenAI client for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# List of models to try (in order of preference)
models_to_try = [
    "deepseek/deepseek-chat-v3.1:free",
    "meta-llama/llama-3.1-8b-instruct:free",
    "microsoft/phi-3-mini-128k-instruct:free",
    "google/gemma-2-9b-it:free",
]

print("\n🧪 Testing models...")
print("Sending test message: 'What is the meaning of life?'\n")

success = False
for model in models_to_try:
    print(f"🔍 Trying: {model}")
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://gym-chatbot.app",
                "X-Title": "Gym Assistant Chatbot",
            },
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "What is the meaning of life?"
                }
            ]
        )
        
        response = completion.choices[0].message.content
        print(f"✅ SUCCESS! Model '{model}' responded:")
        print("-" * 50)
        print(response)
        print("-" * 50)
        print(f"\n🎉 Your API is working correctly with {model}!")
        print(f"\n💡 Tip: Update your .env file with: OPENROUTER_MODEL={model}")
        success = True
        break
        
    except Exception as e:
        error_msg = str(e)
        if "data policy" in error_msg.lower():
            print(f"⚠️  This model requires data policy configuration.")
            print(f"   Configure at: https://openrouter.ai/settings/privacy")
        else:
            print(f"❌ Error: {error_msg[:100]}")
        print()

if not success:
    print("\n❌ None of the tested models worked.")
    print("\n💡 Troubleshooting steps:")
    print("1. Go to https://openrouter.ai/settings/privacy")
    print("2. Configure your data policy for free models")
    print("3. Or use a paid model with your API key")
    print("4. Check your API key is valid and has credits")
