import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def initialize_client():
    """Loads environment variables and initializes the Gemini Client."""
    load_dotenv()
    return genai.Client()

def create_new_chat(client, config: types.GenerateContentConfig):
    """Creates and returns a fresh, stateful chat session with given config."""
    return client.chats.create(model="gemini-2.5-flash", config=config)

def stream_response(chat_session, user_msg: str):
    """Sends a user message to the chat session and streams the response token-by-token."""
    print("\nAI: ", end="", flush=True)
    
    # Request the streaming generator from the SDK
    response_stream = chat_session.send_message_stream(user_msg)
    
    # Stream chunks over the wire immediately
    for chunk in response_stream:
        print(chunk.text, end="", flush=True)
        
    print() # Newline at the end of streaming

def chat_loop():
    """Main application loop managing user input, state commands, and streaming execution."""
    client = initialize_client()
    
    # Configure the system persona
    config = types.GenerateContentConfig(
        system_instruction="You are a brilliant assistant who explains concepts clearly and provides concise, accurate guidance.",
        temperature=0.3
    )
    
    print("=========================================")
    print("     🚀 CAPSTONE CHATBOT (REFACTORED)   ")
    print("  Commands: 'quit' to exit | 'reset' to clean state  ")
    print("=========================================\n")
    
    # Initialize our starting state
    chat_session = create_new_chat(client, config)
    
    while True:
        user_message = input("\nYou: ").strip()
        
        if user_message.lower() == "quit":
            print("\nGoodbye! Clean execution.")
            break
            
        if user_message.lower() == "reset":
            chat_session = create_new_chat(client, config)
            print("\n🔄 Conversation memory cleared! Fresh state initialized.")
            continue
            
        if not user_message:
            continue
            
        try:
            # Call our dedicated streaming function
            stream_response(chat_session, user_message)
            
        except Exception as e:
            print(f"\n⚠️ Temporary disruption occurred: {e}")
            print("Please wait a moment and try your message again.")

# Clear execution trigger when script runs directly
if __name__ == "__main__":
    chat_loop()
    