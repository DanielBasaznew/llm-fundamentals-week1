# Gemini LLM Foundations & Automation Toolkit

A collection of interactive Python tools and scripts built to master LLM APIs, prompt engineering paradigms, stateful chat architectures, and native function-calling mechanics.

## 🛠️ Project Portfolio

*   **Interactive CLI Chatbot (`chatbot.py`):** A command-line companion featuring dynamic multi-turn conversation memory, real-time chunk-streaming delivery, and targeted system instruction styling.
*   **Prompt Engineering Playground (`playground.py`):** A hyperparameter comparison script executing automated testing across distinct temperature settings ($0.0$, $1.0$, $2.0$) to benchmark text creativity and deterministic consistency.
*   **System Time Tool Call (`tool_chat.py`):** A functional prototype utilizing native tool configurations to bind the model directly to local Python execution modules for accessing live system data.

---

## 🚀 Installation & Quick Start

### 1. Clone the Workspace

```bash
git clone https://github.com/DanielBasaznew/llm-fundamentals-week1
cd llm-fundamentals-week1

2. Configure Your Environment Variables
Create a hidden .env file in the root directory to manage your access credentials safely:

Bash
touch .env
Populate your .env file with your secure API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
3. Initialize Runtime Dependencies
Ensure your local system dependencies are updated:

Bash
pip install google-genai python-dotenv
4. Run the Scripts
Execute the scripts using your terminal loop:

Bash
python chatbot.py
python playground.py
python tool_chat.py

##💡 Engineering Insights & Key Takeaways

State Control Management: LLMs are intrinsically stateless. Building an interactive terminal application requires manually assembling and preserving the sequential message arrays (user and model role dictionaries) to sustain consistent context tracking.

Hyperparameter Influence: Tuning generative text engines relies heavily on variables like temperature. Setting it to $0.0$ structures deterministic, analytical results perfect for code pipelines, while setting it to $2.0$ amplifies token randomness for creative generation.

API Security Best Practices: Production keys must never touch the core code logic. Using tools like python-dotenv and locking down environmental files inside .gitignore prevents major security breaches and credential leaks.

Function Binding Horizons: Native tool calling transforms an LLM from a simple prediction engine into an actionable software orchestrator by allowing it to structurally request local system execution when it requires real-world data inputs.