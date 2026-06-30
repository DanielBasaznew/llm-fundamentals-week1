import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Initialize configurations
load_dotenv()
client = genai.Client()

print("=== Welcome to the Prompt Experimenter ===")
print("Type 'exit' at any prompt to quit the program.\n")

# 1. Capture the system instruction once to set the persona
sys_prompt = input("Enter System Instructions (e.g., You are a pirate): ")

if sys_prompt.lower() != 'exit':
    
    # 2. Enter a loop to test multiple prompts under that system instruction
    while True:
        user_msg = input("\nEnter User Message: ")
        if user_msg.lower() == 'exit':
            print("Goodbye!")
            break
            
        # Set up config with the system prompt entered
        config = types.GenerateContentConfig(
            system_instruction=sys_prompt,
            temperature=0.7
        )
        
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_msg,
            config=config,
        )
        
        print("\n--- Response ---")
        print(response.text)