import tiktoken

# 1. Load the standard tokenizer used by OpenAI models (like gpt-4)
encoding = tiktoken.get_encoding("cl100k_base")

# 2. Define a few test sentences to see how they count
text_1 = "Hello, world!"
text_2 = "Tokenization"
text_3 = "Let's see how many tokens this sentence takes."

# 3. Turn the text into tokens (encoding) and print the results
for text in [text_1, text_2, text_3]:
    tokens = encoding.encode(text)
    print(f"\nText: \"{text}\"")
    print(f"Token IDs: {tokens}")
    print(f"Total Count: {len(tokens)} tokens")