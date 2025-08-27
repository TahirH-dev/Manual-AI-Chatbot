import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Wait 2 seconds so you have time to switch to the right screen
time.sleep(2)

# Step 1: Click the chrome icon at (701, 1057)
pyautogui.click(760, 1057)
time.sleep(1)  # wait for app to open

# Step 2: Drag from (637,156) to (1870,966) to select text
pyautogui.moveTo(637, 156)
pyautogui.dragTo(1870, 966, duration=1, button='left')

# Step 3: Copy the selected text (Ctrl + C)
pyautogui.hotkey("ctrl", "c")
pyautogui.click(1262, 657)
time.sleep(0.5)

# Step 4: Get text from clipboard
chat_history = pyperclip.paste()
print("Copied Text:\n", chat_history)

# -----------------------------
# Gemini API Setup
# -----------------------------
API_KEY = "Your Api Key"   # <--- paste your key here    #Tip gemini api is free for 50 request/day
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")  # free, fast model

# Add system-style instruction inside the prompt
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


response = model.generate_content(prompt)
reply_text = response.text.strip()
print("\nGemini Response:\n", response.text)

# -----------------------------
# Step 6: Paste response at specific x,y
# -----------------------------
time.sleep(1)
pyautogui.click(1130, 1000)     # 👈 replace with chatbox coordinates
time.sleep(0.5)

pyperclip.copy(reply_text)      # copy response to clipboard
pyautogui.hotkey("ctrl", "v")   # paste
# pyautogui.press("enter")      # auto-send (optional)