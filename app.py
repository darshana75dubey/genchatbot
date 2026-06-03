import streamlit as st
from google import genai
# pip install streamlit genai
client = genai.Client(
    api_key=st.secrets["AQ.Ab8RN6Ix1Bp4cy-h7zYAQcbULlKeh_4zgiMI0mD3hM9aehy4UQ"]
)
st.title("🤖 Gemini Chatbot")
prompt = st.chat_input("Ask something...")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    with st.chat_message("assistant"):
        st.write(response.text)
