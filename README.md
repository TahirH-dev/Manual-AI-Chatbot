# Manual AI Chatbot 🤖

A set of small Python scripts that demonstrate different ways to automate chat replies using local LLMs (Ollama) and Google Gemini (Generative AI).  
This repo includes both **manual** helper scripts (which only produce the AI reply text) and **automation** scripts that use `PyAutoGUI` to detect/copy the latest chat message and send replies automatically.

> **Important:** These scripts use screen automation (PyAutoGUI). Test carefully — unexpected clicks/typing may interfere with your system. Do NOT commit your `.env` (API keys) or virtual environment.

---

## 🔎 Repository overview (what's inside)
Manual-AI-Chatbot/
├─ 01_get_cursur.py # Cursor helper — get & print screen coordinates for PyAutoGUI
├─ 03_gemini_bot.py # Gemini (manual) — sends prompt to Gemini API, prints answer (manual paste)
├─ 03_ollama_bot.py # Ollama (manual) — sends prompt to local Ollama / prints answer (manual paste)
├─ 04_gemini_bot_auto.py # Gemini (auto) — runs loop, copies last chat message, sends to Gemini and auto-pastes reply
├─ 04_ollama_bot_auto.py # Ollama (auto) — same as above but uses Ollama
├─ requirements.txt # Python dependencies (use with pip install -r requirements.txt)
├─ .gitignore # Ignore venv, .env, caches etc.
└─ README.md # (this file)

### What each script does
- **`01_get_cursur.py`**  
  A tiny helper to show mouse coordinates on your screen. Use it to find correct click/drag coordinates for the auto bots (PyAutoGUI uses coordinates to copy/paste).

- **`03_gemini_bot.py` (manual)**  
  - **`03_gemini_bot.py` (manual)**  
  Sends the copied message to Google Gemini (Generative AI), receives the model's response, and pastes the response into the active text field via the keyboard buffer — you then manually press Enter to send it in your chat app (WhatsApp, Telegram, etc.).

- **`03_ollama_bot.py` (manual)**  
  Same idea as above but sends the prompt to an Ollama model (usually a local model server or local Ollama CLI). Outputs text to console for manual pasting.

- **`04_gemini_bot_auto.py` (auto)**  
  Fully automated loop:
  1. Detects the last message on screen (using PyAutoGUI & clipboard).
  2. If the last message isn't yours, sends it to Gemini.
  3. Automatically pastes the AI answer back to the chat.  
  **Be careful:** this will control your mouse and keyboard.

- **`04_ollama_bot_auto.py` (auto)**  
  Same automation as `04_gemini_bot_auto.py` but uses Ollama for generation.

---

## ⚙️ Requirements
- **Python 3.10+** recommended.
- `pip` available.
- Developer tools (optional): Git, GitHub Desktop.

Dependencies are included in `requirements.txt` — install them in a virtual environment (recommended).

---

## 🚀 Quick start — download & run

### 1) Download the repository
- Option A — clone (recommended if you use git):
  ```bash
  git clone https://github.com/TahirH-dev/Manual-AI-Chatbot.git
  cd Manual-AI-Chatbot

- Option B — download ZIP:
On the repo page click Code → Download ZIP, then extract.

- Option C — download a single file:
Open the file on GitHub → click Raw → save the page (Right click → Save As).

### 2) Create & activate a virtual environment
(keeps dependencies isolated)
python -m venv .venv
# Mac/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate.bat

### 3) Install dependencies
'''bash
pip install -r requirements.txt
'''
### 4) Create .env (local, do NOT commit)
Create a file called .env in the repo root (it is listed in .gitignore). Put your API keys / config there. Example:
'''bash
GEMINI_API_KEY=your_gemini_api_key_here
OLLAMA_API_URL=http://localhost:11434    # or your Ollama server URL
OLLAMA_API_KEY=optional_key_if_needed
'''

The exact variable names may differ depending on the code. Check the top of each script to confirm which environment variables it reads (e.g. os.getenv("GEMINI_API_KEY")).

You can also export environment variables directly in your shell:
'''bash
export GEMINI_API_KEY="your_key_here"
'''

