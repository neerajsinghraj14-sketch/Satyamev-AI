import streamlit as st
import google.generativeai as genai

# Teri Asli API Key (Fixed)
MY_API_KEY = "AIzaSyBnaU5GKOAGN3hhZFc0ZDMfvte0hcS5XKE"

# Setup Gemini AI
try:
    genai.configure(api_key=MY_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("AI Brain load nahi ho raha hai.")

st.set_page_config(page_title="Satyamev AI - Pro", layout="wide")

st.title("🛡️ Satyamev AI: Brain-Powered Protection")
st.write("Ab ye AI scammers ki 'Chalaaki' pakadta hai.")

user_input = st.text_area("Scammer ka message yahan paste karein:", height=200)

if st.button("🚀 DEEP SCAN WITH AI"):
    if user_input:
        with st.spinner('AI dimaag laga raha hai...'):
            try:
                prompt = f"Analyze this message for a scam. Explain in Hinglish (Hindi + English) if it's a scam and give advice. Message: {user_input}"
                response = model.generate_content(prompt)
                st.subheader("AI Analysis Report:")
                st.write(response.text)
            except Exception as e:
                st.error("Kuch technical error hai, thodi der baad try karein.")
    else:
        st.warning("Pehle kuch message toh likho!")

st.sidebar.write("Developed by: **Neeraj Singh**")
