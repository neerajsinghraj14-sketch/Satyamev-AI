import streamlit as st
from google import genai

# Teri API Key
MY_API_KEY = "AIzaSyBnaU5GKOAGN3hhZFc0ZDMfvte0hcS5XKE"

# Version lock taaki 404 error na aaye
try:
    client = genai.Client(api_key=MY_API_KEY, http_options={'api_version': 'v1'})
except Exception as e:
    st.error("AI Setup Failed")

st.set_page_config(page_title="Satyamev AI", layout="wide")

st.title("🛡️ Satyamev AI: Brain-Powered Protection")
st.write("Scammers ki chalaaki pakadne wala AI.")

user_input = st.text_area("Message yahan likhein:", height=200)

if st.button("🚀 DEEP SCAN WITH AI"):
    if user_input:
        with st.spinner('AI dimaag laga raha hai...'):
            try:
                # Direct simple call
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=user_input
                )
                st.subheader("📊 Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Kuch toh likho!")
