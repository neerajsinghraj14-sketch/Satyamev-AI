import streamlit as st

st.set_page_config(page_title="Satyamev AI", page_icon="🛡️")
st.title("🛡️ Satyamev AI: Anti-Scam Guard")
st.write("India ka apna AI jo scammers ko expose karega.")

user_input = st.text_area("Scammer ki line yahan likhein:")

if st.button("Scan Karo"):
    if user_input:
        text = user_input.lower()
        # Scam Detection Logic
        scam_words = ["paisa", "otp", "police", "jail", "block", "lottery", "prize", "khata"]
        is_scam = any(word in text for word in scam_words)
        
        if is_scam:
            st.error("🚨 ALERT: Ye 100% SCAM lag raha hai! Savdhaan rahein.")
        else:
            st.success("✅ Sab normal lag raha hai.")
    else:
        st.warning("Pehle kuch type toh karo bhai!")
