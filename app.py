import streamlit as st
import google.generativeai as genai

# Setup Gemini AI
genai.configure(api_key="YOUR_GEMINI_API_KEY") AIzaSyBnaU5GKOAGN3hhZFc0ZDMfvte0hcS5XKE
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Satyamev AI - Pro", layout="wide")

st.title("🛡️ Satyamev AI: Brain-Powered Protection")
st.write("Ab ye AI sirf words nahi, scammers ki 'Chalaaki' pakadta hai.")

user_input = st.text_area("Scammer ka message ya script yahan likhein:", height=200)

if st.button("🚀 DEEP SCAN WITH AI"):
    if user_input:
        with st.spinner('AI dimaag laga raha hai...'):
            try:
                # AI ko instruction dena
                prompt = f"Analyze this message for a scam. Tell me in Hindi/English if it's a scam and why. Message: {user_input}"
                response = model.generate_content(prompt)
                
                st.subheader("AI Analysis Result:")
                st.write(response.text)
                
                st.divider()
                st.warning("🚨 **Satyamev AI Tip:** Agar AI 'Safe' kahe phir bhi kisi ko paisa mat bhejna.")
            except Exception as e:
                st.error("API Key shayad sahi nahi hai, ek baar check karo.")
    else:
        st.warning("Bhai, pehle message toh dalo!")

st.sidebar.write("Developed by: **Neeraj Singh**")
