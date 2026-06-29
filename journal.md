# Day 1 Journal: Tokenization Insights

Today I discovered that language models don't read complete words. Instead, they process text in chunks called tokens. 

What surprised me:
- The single word "Tokenization" is actually viewed as 2 tokens by the model.
- Punctuation marks like `!` and `,` take up token slots, meaning shorter-looking text can have a higher token count than expected.
- The surprising insight that I gain today is because of most AI models traind on English language they will split to many small chanks for a language rather than English and this lead to token runing out early.