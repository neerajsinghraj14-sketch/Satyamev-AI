import streamlit as st

# Page configuration
st.set_page_config(page_title="Satyamev AI - Anti-Scam", page_icon="🛡️")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; }
    .main { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Satyamev AI: Anti-Scam Guard")
st.subheader("India ko digital thagi se bachane ki ek pehal")
st.write("---")

# Input area
user_input = st.text_area("Scammer ka message ya call ki baatein yahan likhein:", 
                         placeholder="Jaise: Aapka account block ho gaya hai, OTP dein...",
                         height=150)

if st.button("🚨 SCAN KARO"):
    if user_input:
        text = user_input.lower()
        
        # Scam Keywords List
        scam_words = [
            "otp", "paisa", "account block", "lottery", "prize", "gift", "cbi", 
            "police", "arrest", "kyc", "bank", "bill", "link", "click", "pan card"
        ]
        
        found = [word for word in scam_words if word in text]
        
        if found:
            st.error(f"### 🛑 MAHA-SCAM DETECTED!")
            st.write(f"Humne ye sandigdh shabd pakde hain: **{', '.join(found)}**")
            st.warning("**Foran ye karein:**\n1. Kisi bhi link par click na karein.\n2. Phone turant kaat dein.\n3. Koi bhi app install na karein.")
            
            st.write("---")
            st.info("📢 **Kahan Shikayat Karein?**\n\n* **Helpline:** Dial **1930**\n* **Website:** [cybercrime.gov.in](https://cybercrime.gov.in)")
        else:
            st.success("✅ **SAFE:** Abhi tak kuch bhi suspicious nahi mila. Savdhaan rahein!")
    else:
        st.warning("Bhai, pehle kuch message toh likho!")

# Sidebar for Branding
st.sidebar.title("Satyamev AI")
st.sidebar.info("Ye tool scammers ko expose karne ke liye banaya gaya hai.")
st.sidebar.write("---")
st.sidebar.write("Developed by: **Neeraj Singh**")
