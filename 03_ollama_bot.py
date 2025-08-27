import pyautogui
import pyperclip
import time
import requests
import json

# -----------------------------
# Step 1: Wait 2 seconds so you can switch to chat screen
# -----------------------------
time.sleep(2)

# Step 2: Click the chrome icon at (701, 1057)
pyautogui.click(761, 1057)
time.sleep(1)  # wait for app to open

# Step 3: Drag from (637,156) to (1870,966) to select text
pyautogui.moveTo(637, 156)
pyautogui.dragTo(1870, 966, duration=1, button='left')

# Step 4: Copy the selected text (Ctrl + C)
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
You are a person named Tahir from Pakistan.  
You speak a mix of Urdu and English naturally, just like in real WhatsApp chats.  
Analyze the chat history and reply as if you are Tahir continuing the conversation.  

Rules:  
- Write casually, not too formal.  
- Mix Urdu + English where it feels natural.  
- Keep responses short or medium, like real chat (not essays).  
- Use emojis 🙂😂🔥 only when it fits the mood.  
- Add little human touches (like "hmm", "acha", "yaar", "btw").  
- Don’t repeat the whole question, just reply like a normal chat.  
- Sometimes make small spelling shortcuts like real WhatsApp typing (e.g. “tm”, “acha”, “oky”).  

Chat History:
{chat_history}
"""

payload = {
    "model": "gemma:2b",  # 👈 change model if you like
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)
data = response.json()
reply_text = data.get("response", "").strip()

print("\nOllama Response:\n", reply_text)

# -----------------------------
# Step 7: Paste response into chatbox
# -----------------------------
time.sleep(1)
pyautogui.click(1130, 1000)  # 👈 replace with your chatbox coordinates
time.sleep(0.5)

pyperclip.copy(reply_text)   # copy response to clipboard
pyautogui.hotkey("ctrl", "v")  # paste
# pyautogui.press("enter")     # auto-send (optional)
