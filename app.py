import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

config = types.GenerateContentConfig(
    system_instruction="You are a helpful assistant.",
    temperature=0.2  # Keep it low so it focuses tightly on our example pattern
)

# Structuring the few-shot examples as historical conversation context
few_shot_contents = [
    types.Content(role="user", parts=[types.Part(text="Convert apple to a secret code")]),
    types.Content(role="model", parts=[types.Part(text="CODE: A-P-P-L-E")]),
    types.Content(role="user", parts=[types.Part(text="Convert banana to a secret code")]),
    types.Content(role="model", parts=[types.Part(text="CODE: B-A-N-A-N-A")]),
    # This is our real question following the pattern:
    types.Content(role="user", parts=[types.Part(text="Convert coffee to a secret code")]),
]

print("Sending message with few-shot examples...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=few_shot_contents,
    config=config,
)

print("\n--- Response ---")
print(response.text)