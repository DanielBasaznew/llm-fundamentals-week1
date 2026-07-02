# Day 1 Journal: Tokenization Insights

Today I discovered that language models don't read complete words. Instead, they process text in chunks called tokens. 

What surprised me:
- The single word "Tokenization" is actually viewed as 2 tokens by the model.
- Punctuation marks like `!` and `,` take up token slots, meaning shorter-looking text can have a higher token count than expected.
- The surprising insight that I gain today is because of most AI models traind on English language they will split to many small chanks for a language rather than English and this lead to token runing out early.

## Day 2 Journal: Prompt Engineering & Control

Today I learned how to guide and constrain an LLM's outputs using system instructions, temperature configurations, and few-shot examples.

What I observed:
- **System Instructions:** Giving the model a persona (like a sarcastic assistant) completely shifts its tone and vocabulary.
- **Temperature:** Cranking the temperature up to `1.5` forced the model to generate much more expressive, creative, and descriptive narratives.
- **Few-Shot Prompting:** Providing structural examples inside the conversation list taught the model exactly how to format its response without me needing to explain the rules explicitly.

## Day 3 Journal: State Management & Chat History

Today I built a full back-and-forth terminal chatbot and learned how stateful conversation memory works under the hood.

What I observed:
- **Simulating Memory:** LLMs are naturally stateless. To make them remember, we have to keep a continuous record of the conversation state and send the entire history context with every new message.
- **State Manipulation:** By overriding the chat object variable when the user types `reset`, we can completely clear the local conversation state and start fresh without restarting the application backend.

## Day 4 Journal: Streaming Responses & Final Polish


What I observed:
- **Streaming Impact:** Streaming makes the app feel completely fluid and responsive. The perceived latency drops dramatically because the user gets feedback instantly.
- **Terminal vs. Real Products:** While our terminal chatbot handles text perfectly, real applications like ChatGPT can render Markdown beautifully (like converting `**` to bold text), handle file/image uploads, and format source code into dedicated copy-paste boxes.