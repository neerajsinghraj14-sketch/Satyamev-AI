import streamlit as st
import google.generativeai as genai

# Teri API Key maine yahan set kar di hai
MY_API_KEY = "AIzaSyBnaU5GKOAGN3hhZFc0ZDMfvte0hcS5XKE"

# Setup Gemini AI
try:
    genai.configure(api_key=MY_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("AI Setup mein dikat aa rahi hai.")

st.set_page_config(page_title="Satyamev AI - Futuristic Shield", page_icon="🛡️", layout="wide")

st.title("🛡️ Satyamev AI: Next-Gen Anti-Scam Engine")
st.markdown("### *India ka Sabse Smart AI Bodyguard*")
st.write("---")

# Dynamic Ticker
st.warning("🔥 **LATEST THREAT:** Digital Arrest aur FedEx Parcel scam se bachein. Police kabhi video call par arrest nahi karti!")

# Scanner Layout
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Scammer ka message ya call ki baatein yahan likhein:", 
                             height=250, 
                             placeholder="Example: Aapka bank account block hone wala hai...")
    
    if st.button("🚀 DEEP SCAN (AI ANALYZE)"):
        if user_input:
            with st.spinner('Satyamev AI dimaag laga raha hai...'):
                try:
                    # AI ko instruction dena
                    prompt = f"""
                    You are a professional Cyber Security Expert. 
                    Analyze this message for a potential scam: "{user_input}"
                    Explain in Hinglish (Hindi + English) if it is a scam or safe.
                    Give 3 clear reasons and an action plan.
                    """
                    response = model.generate_content(prompt)
                    
                    st.subheader("📊 AI Analysis Report:")
                    st.write(response.text)
                    
                    st.divider()
                    st.info("💡 **Pro Tip:** Agar AI 'Neutral' dikhaye par wo paisa maange, toh wo 100% scam hai.")
                except Exception as e:
                    st.error("Service busy hai ya API Key update ho rahi hai. Thodi der baad try karein.")
        else:
            st.warning("Bhai, pehle kuch text toh dalo!")

with col2:
    st.subheader("🌐 Security Center")
    st.write("Current Safety Level: **High**")
    st.divider()
    st.info("📢 **Emergency Helpline:** Dial **1930**")
    st.markdown("[Report on CyberCrime.gov.in](https://cybercrime.gov.in)")
    st.divider()
    if st.button("🚩 Report New Scam Type"):
        st.write("Thank you! Hum ise database mein add karenge.")

st.write("---")
st.caption("Developed by Neeraj Singh | Satyamev AI Project 2026")
