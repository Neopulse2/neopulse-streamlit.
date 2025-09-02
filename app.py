import streamlit as st
import requests
from textblob import TextBlob

st.set_page_config(page_title="NeoPulse Dashboard", layout="centered")
st.title("🎛 NeoPulse Media Control")

# 🔹 YouTube Upload Section
st.header("📤 Upload to YouTube")
video = st.file_uploader("Choose video file", type=["mp4", "mov", "avi"])
title = st.text_input("Video Title")
desc = st.text_area("Video Description")

if st.button("Upload to YouTube"):
    if video and title:
        st.success(f"✅ '{title}' uploaded to YouTube!")  # Replace with actual API logic
    else:
        st.error("⚠ Please provide both video and title.")

# 🔹 TikTok Trigger Section
st.header("🎵 Post to TikTok")
tiktok_url = st.text_input("TikTok Webhook URL")
caption = st.text_input("TikTok Caption")

if st.button("Trigger TikTok Post"):
    if tiktok_url and caption:
        try:
            response = requests.post(tiktok_url, json={"caption": caption})
            if response.status_code == 200:
                st.success("✅ TikTok post triggered!")
            else:
                st.error(f"❌ Error: {response.status_code}")
        except Exception as e:
            st.error(f"⚠ Failed to send request: {e}")
    else:
        st.warning("Please enter both webhook URL and caption.")

# 🔹 Auto-Reply Engine
st.header("💬 Persona Reply Generator")
comment = st.text_input("Incoming Comment")

def generate_reply(text):
    sentiment = TextBlob(text).sentiment.polarity
    text_lower = text.lower()
    if "🔥" in text or sentiment > 0.5:
        return "Glad you're loving it! More heat coming 🔥"
    elif "❤" in text or sentiment > 0.2:
        return "Appreciate the love! You're amazing ❤"
    elif "❓" in text or "?" in text or sentiment < 0:
        return "Great question! Here's the answer..."
    elif "hate" in text_lower or sentiment < -0.3:
        return "Thanks for the feedback — we’re always improving 💡"
    else:
        return "Thanks for engaging! Stay tuned 🚀"

if comment:
    reply = generate_reply(comment)
    st.write(f"🧠 Suggested Reply: {reply}")
  import streamlit as st
import requests
from textblob import TextBlob
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]  # Store your key in Streamlit secrets

st.set_page_config(page_title="NeoPulse Dashboard", layout="centered")
st.title("🎛 NeoPulse Media + Chat Assistant")

# 🔹 YouTube Upload Section
st.header("📤 Upload to YouTube")
video = st.file_uploader("Choose video file", type=["mp4", "mov", "avi"])
title = st.text_input("Video Title")
desc = st.text_area("Video Description")

if st.button("Upload to YouTube"):
    if video and title:
        st.success(f"✅ '{title}' uploaded to YouTube!")  # Replace with actual API logic
    else:
        st.error("⚠ Please provide both video and title.")

# 🔹 TikTok Trigger Section
st.header("🎵 Post to TikTok")
tiktok_url = st.text_input("TikTok Webhook URL")
caption = st.text_input("TikTok Caption")

if st.button("Trigger TikTok Post"):
    if tiktok_url and caption:
        try:
            response = requests.post(tiktok_url, json={"caption": caption})
            if response.status_code == 200:
                st.success("✅ TikTok post triggered!")
            else:
                st.error(f"❌ Error: {response.status_code}")
        except Exception as e:
            st.error(f"⚠ Failed to send request: {e}")
    else:
        st.warning("Please enter both webhook URL and caption.")

# 🔹 Auto-Reply Engine
st.header("💬 Persona Reply Generator")
comment = st.text_input("Incoming Comment")

def generate_reply(text):
    sentiment = TextBlob(text).sentiment.polarity
    text_lower = text.lower()
    if "🔥" in text or sentiment > 0.5:
        return "Glad you're loving it! More heat coming 🔥"
    elif "❤" in text or sentiment > 0.2:
        return "Appreciate the love! You're amazing ❤"
    elif "❓" in text or "?" in text or sentiment < 0:
        return "Great question! Here's the answer..."
    elif "hate" in text_lower or sentiment < -0.3:
        return "Thanks for the feedback — we’re always improving 💡"
    else:
        return "Thanks for engaging! Stay tuned 🚀"

if comment:
    reply = generate_reply(comment)
    st.write(f"🧠 Suggested Reply: {reply}")

# 🔹 ChatGPT Assistant
st.header("🧠 Ask NeoPulse Anything")
input_text = st.text_input("Ask me anything")

def generate_chat_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ]
    )
    return response['choices'][0]['message']['content']

if input_text:
    st.write("Thinking...")
    response = generate_chat_response(input_text)
    st.write(response)
