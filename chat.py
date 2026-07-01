import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load environment variables and initialize client
load_dotenv()
client = genai.Client()

print("=== Starting Day 3 Chat Session ===")
print("Type 'quit' to exit, or 'reset' to clear memory.\n")

# 2. Initialize our stateful chat session
chat = client.chats.create(model="gemini-2.5-flash")

# 3. Enter the continuous messaging loop
while True:
    # Capture user input from the terminal
    user_message = input("\nYou: ")
    
    # Check if the user wants to leave
    if user_message.strip().lower() == "quit":
        print("Goodbye!")
        break
        
    # NEW: Check if the user wants to wipe the memory
    if user_message.strip().lower() == "reset":
        print("\n--- Memory Cleared! Starting a fresh session. ---")
        # Re-initialize the chat object to clear the history array
        chat = client.chats.create(model="gemini-2.5-flash")
        continue
        
    # Skip empty lines
    if not user_message.strip():
        continue
        
    print("AI is typing...")
    
    # 4. Send the message through the stateful chat object
    response = chat.send_message(user_message)
    
    # 5. Print out the response cleanly
    print(f"\nAI: {response.text}")