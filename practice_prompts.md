# Week 1: Prompt Engineering Practice Portfolio

## Task 1 — Summarization

### Original Article Source / Topic:
An article discussing how the wives and girlfriends (WAGs) of soccer players have evolved into massive global fashion and style icons ahead of the FIFA World Cup 2026.

### 1-Sentence Summary Prompt & Output:
- **Prompt:** "Summarize this article in exactly one sentence: [Article Text]"
- **Output:** Ahead of the FIFA World Cup 2026, the players' wives and girlfriends (WAGs) are capturing significant global media attention by evolving into influential style and lifestyle icons who tightly merge the worlds of elite sports and high fashion.

### 3-Bullet Points Prompt & Output:
- **Prompt:** "Summarize this article in 3 clear bullet points: [Article Text]"
- **Output:** * **Cultural Integration:** WAGs are deeply embedded in modern soccer culture, drawing as much media spotlight off the pitch as the players do on it.
  * **Fashion & Commercial Drivers:** Through game-day outfits and VIP-suite appearances, they act as major style icons driving heavy consumer interest and social media engagement.
  * **Global Spectacle:** Their presence elevates the World Cup from a purely athletic competition into a multi-faceted global entertainment and lifestyle event.

### 10-Year-Old Summary Prompt & Output:
- **Prompt:** "Summarize this article so a 10-year-old can easily understand it: [Article Text]"
- **Output:** When the big soccer World Cup starts, it's not just the players getting famous! Their wives and girlfriends (called WAGs) become super popular too. They dress up in really cool clothes, go to the games, and post on social media. People love watching what they wear, which turns the giant soccer tournament into a massive fashion show!

---

## Task 2 — Translation

### Standard Translation Prompt & Output:
- **Prompt:** "Translate this standard text into clear Amharic: 'In the modern era, sport and fashion are inexorably entwined. WAGs serve as style icons, and their game-day outfits drive consumer interest.'"
- **Output:** በዘመናዊው ዘመን፣ ስፖርት እና ፋሽን በማይነጣጠል መልኩ የተሳሰሩ ናቸው። የተጫዋቾች ሚስቶች እና የሴት ጓደኞች (WAGs) የፋሽን ተምሳሌት ሆነው ያገለግላሉ፣ እንዲሁም በጨዋታ ቀን የሚለብሷቸው አልባሳት የሸማቾችን ፍላጎት ያነሳሳሉ።

### Idiom/Nuance Translation Prompt & Output:
- **Prompt:** "Translate this phrase into Amharic, but preserve the true meaning instead of translating it literally: 'He was completely over the moon when he heard the news, but his brother told him to rain on his parade.'"
- **Output:** ዜናውን ሲሰማ ደስታው ወደር አልነበረውም (በጣም ተደስቶ ነበር)፤ ነገር ግን ወንድሙ ስሜቱን አበረደበት (ደስታውን አበላሸበት)።
  
  *Note on Cultural Context:* The model correctly recognized that "over the moon" means extreme joy and "rain on his parade" means ruining someone's moment or dampening their spirits, avoiding a broken literal translation about physical rain and the lunar orbit.

---

## Task 3 — Code Generation

### Palindrome Check Prompt & Output:
- **Prompt:** "Write a Python function that takes a string and checks if it is a palindrome (reads the same backwards as forwards). Include a couple of test cases."
- **Output:**
```python
def is_palindrome(text: str) -> bool:
    """Checks if a normalized string reads the same backwards as forwards."""
    # Remove whitespace and convert to lowercase for fair evaluation
    clean_text = "".join(text.split()).lower()
    return clean_text == clean_text[::-1]

# Test Cases
print(is_palindrome("racecar"))  # Expected: True
print(is_palindrome("radar"))    # Expected: True
print(is_palindrome("python"))   # Expected: False
print(is_palindrome("A man a plan a canal Panama")) # Expected: True

Task 4 — Debugging
Broken Code Prompt & Output:
Prompt: "Find the bugs in this Python code, explain why they break the execution, and give me the corrected snippet:

Python
def calculate_area(width, height)
area = width * height
   return Area
```"
- **Output:** There are three specific issues breaking this execution:
1. **Missing Syntax Colon:** The function header `def calculate_area(width, height)` is missing a trailing `:` to define the code block.
2. **Indentation Error:** The variable assignment `area = width * height` must be indented by 4 spaces to reside inside the function scope.
3. **Name/Case Error:** Python is case-sensitive. The function assigns the result to lowercase `area`, but tries to return capitalized `Area`, which throws a `NameError`.

**Corrected Code:**
```python
def calculate_area(width, height):
    area = width * height
    return area
Task 5 — Brainstorming
Basic Prompt & Output:
Prompt: "Give me 10 names for a coding bootcamp."

Output:

CodeAcademy

TechBootcamp

LearnToCode

ByteSize Coding

DevSchool

Programmers Hub

The Coding School

Software Craft

Alpha Developers

WebDev Academy

Optimized Strategic Prompt & Output:
Prompt: "Act as an elite brand strategist. Give me 10 unique, highly memorable, and modern names for a coding bootcamp targeting self-taught developers. Avoid generic words like 'Tech', 'Code', or 'Academy'. Make them punchy and short."

Output:

Forge (Evokes raw building, molding, and creation)

Syntax (Minimalist, core engineering foundational element)

Unbound (Represents breaking free from non-traditional routes)

Foundry (A workshop where raw elements are cast into steel tools)

Compile (Punchy software action that brings logic together)

Vector (Indicates moving forward with speed and direction)

Apex (Targeting reaching the peak of their self-taught journey)

Shift (Represents a career pivot or perspective change)

Artifact (Beautifully engineered building outputs)

Kinetik (Symbolizes movement, energy, and rapid progress)

