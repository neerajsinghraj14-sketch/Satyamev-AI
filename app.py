import streamlit as st

# Page setup
st.set_page_config(page_title="Satyamev AI - Anti-Scam", page_icon="🛡️")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Satyamev AI: Anti-Scam Guard")
st.write("India ka apna AI jo aapko digital thagi se bachayega.")
st.write("---")

# Input Box
user_input = st.text_area("Scammer ka message ya call ki baatein yahan paste karein:", 
                         placeholder="Example: Aapka KYC expire ho gaya hai, turant update karein...",
                         height=150)

if st.button("🚨 SCAN KARO"):
    if user_input:
        text = user_input.lower()
        
        # Advanced Scam Keywords
        scam_keywords = [
            "otp", "paisa", "account block", "lottery", "prize", "gift", "cbi", "police", 
            "arrest", "kyc", "bank", "customer care", "electricity", "bill", "link", "click"
        ]
        
        found = [word for word in scam_keywords if word in text]
        
        if found:
            st.error(f"### 🛑 ALERT: YE EK SCAM HAI!")
            st.write(f"Humne ye khatarnak words pakde hain: **{', '.join(found)}**")
            st.warning("**Foran ye karein:**\n1. Kisi bhi link par click mat karein.\n2. Koi bhi OTP share na karein.\n3. Is number ko block kar dein.")
            
            st.write("---")
            st.subheader("📢 Turant Sahayata Ke Liye:")
            st.info("Cyber Crime Helpline: **Dial 1930**")
            st.markdown("[Official Complaint Website](https://cybercrime.gov.in)")
        else:
            st.success("✅ **SAFE LAG RAHA HAI:** Humein koi scam keywords nahi mile. Phir bhi savdhaan rahein!")
    else:
        st.warning("Bhai, pehle kuch message toh likho!")

# Sidebar Info
st.sidebar.title("About Satyamev AI")
st.sidebar.info("Ye tool aapki safety ke liye banaya gaya hai. Har mahine 10,000+ log digital scam ka shikaar hote hain. Hum ise milkar rokenge!")
st.sidebar.write("---")
st.sidebar.write("Developed with ❤️ by **Neeraj Singh**")
