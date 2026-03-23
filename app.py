import streamlit as st

st.set_page_config(page_title="Satyamev AI", page_icon="🛡️", layout="centered")

# Design & Header
st.title("🛡️ Satyamev AI: Anti-Scam Guard")
st.subheader("India ka sabse asaan Scam Detection tool")
st.write("---")

# User Input Section
user_input = st.text_area("Scammer ka message ya call ki baatein yahan likhein:", height=150, placeholder="Jaise: Aapka bank account block ho gaya hai...")

if st.button("🚨 AI SCAN KARO"):
    if user_input:
        text = user_input.lower()
        
        # Power Logic
        danger_words = ["paisa", "otp", "police", "jail", "block", "lottery", "prize", "khata", "arrest", "kyc", "cbi"]
        found = [word for word in danger_words if word in text]
        
        if found:
            st.error(f"### 🛑 MAHA-SCAM DETECTED!")
            st.write(f"Humne ye khatarnak shabd pakde hain: **{', '.join(found)}**")
            st.warning("👉 **ACTION:** Phone kaat do aur koi bhi link mat dabao!")
            
            # Emergency Help
            st.write("---")
            st.info("📢 **Kahan Shikayat Karein?**\n\n* **Helpline:** Dial **1930** (Cyber Crime Cell)\n* **Website:** [cybercrime.gov.in](https://cybercrime.gov.in)")
        else:
            st.success("✅ **SAFE:** Abhi tak kuch bhi suspicious nahi mila. Par savdhaan rahein!")
    else:
        st.warning("Bhai, pehle kuch likho toh sahi!")

# Sidebar for Trust
st.sidebar.title("Mission: Scam-Free India")
st.sidebar.write("Ye AI aapko digital dhokhadhari se bachane ke liye banaya gaya hai.")
st.sidebar.markdown("---")
st.sidebar.write("DEVELOPED BY: **NEERAJ SINGH**")
