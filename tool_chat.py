import datetime
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Initialize environment variables and the client
load_dotenv()
client = genai.Client()

# 2. Define the local Python function the model can call
# We write a clear docstring because the model reads it to understand what the tool does!
def get_current_time() -> str:
    """Returns the current date and time on the local computer system."""
    now = datetime.datetime.now()
    return f"The current system time is: {now.strftime('%I:%M %p on %A, %B %d, %Y')}"

# 3. Put our function into the tools list config
config = types.GenerateContentConfig(
    system_instruction="You are a helpful assistant. Use tools when necessary to get accurate current info.",
    temperature=0.0, # Keep temperature at 0.0 for reliable tool usage
    tools=[get_current_time] # Passing our python function directly here
)

print("=== Tool Calling Proof of Concept ===")
user_msg = "Hey, what time is it right now?"
print(f"User Question: '{user_msg}'")
print("Processing request (Model determining if it needs tools)...")

# 4. Generate content with the tools configuration attached
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=user_msg,
    config=config
)

print("\n--- Final Model Response ---")
print(response.text)