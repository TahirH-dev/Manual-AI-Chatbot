import pyautogui
import pyperclip
import time
import requests
import json

# -----------------------------
# Step 1: Wait 2 seconds so you can switch to chat screen
# -----------------------------
time.sleep(2)

# Step 2: Click the Chrome icon (adjust coords)
pyautogui.click(761, 1057)
time.sleep(1)

# Step 3: Drag to select chat text (adjust coords)
pyautogui.moveTo(637, 156)
pyautogui.dragTo(1870, 966, duration=1, button='left')

# Step 4: Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Step 5: Get text from clipboard
chat_history = pyperclip.paste()
print("Copied Text:\n", chat_history)

# -----------------------------
# Step 6: Ollama API call
# -----------------------------
url = "http://localhost:11434/api/generate"

prompt = f"""
You are Tahir, a Pakistani who speaks Urdu + English like in WhatsApp chats.  
Read the chat history and continue the conversation naturally.  

Rules:
- Keep replies casual and short-medium (not essays).
- Mix Urdu + English (code-switching).
- Use emojis only if natural 🙂😂🔥.
- Add human fillers ("hmm", "acha", "yaar", "btw").
- Sometimes use WhatsApp-style shortcuts ("tm", "acha", "oky").
- Reply like a real chat, not formal writing.

Chat History:
{chat_history}
"""

payload = {
    "model": "gemma:2b",   # 👈 use any Ollama model you have (e.g. "llama3", "phi3", etc.)
    "prompt": prompt,
    "stream": False
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    reply_text = data.get("response", "").strip()
except Exception as e:
    print("Error from Ollama:", e)
    reply_text = "Net issue aa gyi lagta hai 😅"

print("\nOllama Response:\n", reply_text)

# -----------------------------
# Step 7: Paste response into chatbox
# -----------------------------
time.sleep(1)
pyautogui.click(1130, 1000)  # 👈 replace with your chatbox coords
time.sleep(0.5)

pyperclip.copy(reply_text)   # copy response to clipboard
pyautogui.hotkey("ctrl", "v")  # paste
pyautogui.press("enter")     # auto-send (optional)
