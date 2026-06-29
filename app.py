import os
from google import genai
from dotenv import load_dotenv

# 1. Load the secret API key from the .env file
load_dotenv()

# 2. Initialize the client (it automatically looks for GEMINI_API_KEY)
client = genai.Client()

# 3. Send a single hardcoded message to the model
print("Sending message to Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Hello! Who are you and what can you do?',
)

# 4. Print the response text to your screen
print("\n--- Response ---")
print(response.text)