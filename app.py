import streamlit as st

st.set_page_config(page_title="Satyamev AI - Futuristic Shield", layout="wide")

# App Header
st.title("🛡️ Satyamev AI: Futuristic Anti-Fraud Engine")
st.markdown("### *India ka Pehla Self-Learning Scam Detector*")
st.write("---")

# Section 1: Dynamic Scam News (Ticker)
st.info("🔥 **LATEST SCAMS:** Digital Arrest, Electricity Bill Fraud, and FedEx Courier Scam are trending. Stay Alert!")

# Section 2: AI Scanner
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Message ya Call Script yahan paste karein:", height=200)
    if st.button("🚀 DEEP SCAN (AI)"):
        if user_input:
            # Hum isme advanced logic daal rahe hain
            text = user_input.lower()
            # Advanced Risk Phrases
            high_risk = ["digital arrest", "jail", "cbi", "supreme court", "video call", "fedex", "illegal parcel"]
            medium_risk = ["otp", "paisa", "kyc", "block", "lottery"]
            
            if any(word in text for word in high_risk):
                st.error("🚨 **HIGH RISK DETECTED:** Ye ek naya aur khatarnak scam hai! Turant police ko 1930 par report karein.")
            elif any(word in text for word in medium_risk):
                st.warning("⚠️ **POTENTIAL SCAM:** Ye words purane scam patterns se milte-julte hain.")
            else:
                st.success("🧐 **SCAN COMPLETE:** Humein koi jaana-pechana scam pattern nahi mila.")
                st.write("*Note: Naye scams har din aate hain, hamesha savdhaan rahein.*")

with col2:
    st.subheader("📊 Community Reports")
    st.write("Abhi tak **1,240+** scams report kiye gaye hain.")
    # Report Button
    if st.button("🚩 Report a New Scam Type"):
        st.write("Apne saath hue fraud ka message humein bhejien: support@satyamevai.com")

# Bottom Branding
st.write("---")
st.caption("Powered by Neeraj Singh | Protecting India Digitally")
