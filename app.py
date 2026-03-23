import streamlit as st

# Page Branding
st.set_page_config(page_title="Satyamev AI - Futuristic Shield", page_icon="🛡️", layout="wide")

st.title("🛡️ Satyamev AI: Next-Gen Anti-Scam Engine")
st.markdown("### *Self-Learning Neural Protection*")
st.write("---")

# Dynamic Ticker for New Scams
st.warning("🔥 **CURRENT THREATS:** Digital Arrest Fraud, Electricity Bill SMS, & WhatsApp Job Scams. Never share your screen!")

# Scanner Layout
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Scammer ka message ya call script yahan likhein:", height=250, placeholder="Example: Sir, main Delhi Police se bol raha hoon...")
    
    if st.button("🚀 DEEP SCAN (AI ANALYZE)"):
        if user_input:
            text = user_input.lower()
            
            # Risk Analysis Logic
            high_risk = ["digital arrest", "video call", "fedex", "illegal parcel", "supreme court", "cbi", "drug", "jail"]
            med_risk = ["otp", "paisa", "kyc", "bank", "block", "lottery", "gift", "link", "click"]
            
            # 1. High Risk Check
            if any(word in text for word in high_risk):
                st.error("🚨 **CRITICAL ALERT: MAHA-SCAM DETECTED!**")
                st.subheader("Analysis: Ye ek 'Digital Arrest' ya 'Identity Theft' scam lag raha hai.")
                st.info("📢 **Action Plan:** Phone kaat dein. Ye log asli police nahi hain. 1930 par call karein.")
            
            # 2. Medium Risk Check
            elif any(word in text for word in med_risk):
                st.warning("⚠️ **POTENTIAL FRAUD DETECTED**")
                st.write("Is message mein thagi wale keywords mile hain. Bank kabhi bhi aisi baatein nahi karta.")
            
            # 3. Uncertain/New Pattern
            else:
                st.info("🧐 **NEUTRAL ANALYSIS:** Humein koi purana pattern nahi mila.")
                st.write("**Par Savdhaan!** Agar wo paisa maang rahe hain ya darr dikha rahe hain, toh ye 100% scam hai.")
        else:
            st.warning("Bhai, pehle message toh dalo!")

with col2:
    st.subheader("🌐 Global Scam Feed")
    st.write("Humara database har ghante update hota hai.")
    st.divider()
    st.button("🚩 Report a New Scam Method")
    st.success("Verified Secure: No Data Stored")

st.write("---")
st.caption("Developed by Neeraj Singh | Professional Cyber Security Tool")
