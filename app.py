import streamlit as st
from google import genai

# Teri API Key (Fixed)
MY_API_KEY = "AIzaSyBnaU5GKOAGN3hhZFc0ZDMfvte0hcS5XKE"

# Setup New Gemini Client
try:
    client = genai.Client(api_key=MY_API_KEY)
except Exception as e:
    st.error("AI setup mein dikkat hai.")

st.set_page_config(page_title="Satyamev AI - Pro", layout="wide")

st.title("🛡️ Satyamev AI: Next-Gen Protection")
st.write("India ka apna AI jo scammers ki 'Chalaaki' pakadta hai.")

user_input = st.text_area("Scammer ka message yahan paste karein:", height=200)

if st.button("🚀 DEEP SCAN WITH AI"):
    if user_input:
        with st.spinner('Satyamev AI dimaag laga raha hai...'):
            try:
                # Fixed model name for the new library
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=f"Analyze this message for a scam. Explain in Hinglish (Hindi + English) if it's a scam and give advice. Message: {user_input}"
                )
                
                st.subheader("📊 AI Analysis Report:")
                st.write(response.text)
                
                st.divider()
                st.info("📢 Help: Dial 1930 for Cyber Crime.")
            except Exception as e:
                # Agar phir bhi error aaye, toh error message dikhayega
                st.error(f"Technical Error: {e}")
    else:
        st.warning("Pehle kuch message toh likho!")

st.sidebar.write("Developed by: **Neeraj Singh**")
