import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Initialize environments and client
load_dotenv()
client = genai.Client()

# 2. Configure our system persona and low temperature for accuracy
config = types.GenerateContentConfig(
    system_instruction="You are a brilliant assistant who explains concepts clearly and provides concise, accurate guidance.",
    temperature=0.3
)

print("=========================================")
print("     🚀 CAPSTONE CHATBOT GENERATION     ")
print("  Commands: 'quit' to exit | 'reset' to clean state  ")
print("=========================================\n")

# 3. Create our starting chat session with our config loaded
chat = client.chats.create(model="gemini-2.5-flash", config=config)

while True:
    user_message = input("\nYou: ")
    
    if user_message.strip().lower() == "quit":
        print("\nGoodbye! Excellent building this week.")
        break
        
    if user_message.strip().lower() == "reset":
        chat = client.chats.create(model="gemini-2.5-flash", config=config)
        print("\n🔄 Conversation memory cleared! Fresh state initialized.")
        continue
        
    if not user_message.strip():
        continue
        
    print("\nAI: ", end="", flush=True)
    
    try:
        # 4. Request a streaming response chunk by chunk
        response_stream = chat.send_message_stream(user_message)
        
        # 5. Loop over the text chunks as they fly over the network
        for chunk in response_stream:
            # print without adding newlines, and use flush=True to bypass buffering
            print(chunk.text, end="", flush=True)
            
        print() # Print an empty line at the end of the streaming response
        
    except Exception as e:
        print(f"\n⚠️ Temporary disruption occurred: {e}")
        print("Please wait a moment and try your message again.")