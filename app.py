# A streamlit app to display a chat bot using GPT3.5 turbo model for my friend Matt who is a dog trainer
import streamlit as st
import os
from utils.chat2 import initiate_bot
from dotenv import load_dotenv
load_dotenv()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []



st.subheader("Chat with MattGPT")

question = st.text_input("Type your message to Matt here")
send_button = st.button("Send")
if send_button:
    # Add a spinner to let the user know that the app is working
    with st.spinner("Matt is thinking..."):
        initiate_bot(question)
        for message in st.session_state.display_messages:
            st.write(message)




