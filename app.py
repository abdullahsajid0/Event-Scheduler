import streamlit as st
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Initialize MistralAI client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key is not set. Please configure the GROQ_API_KEY environment variable.")
else:
    model = "mistral-large-latest"
    client = MistralClient(api_key=api_key)

# Streamlit UI
st.title("Schedule Assistant")
st.write("Get a schedule to manage effectively.")

# User input
user_input = st.text_input("Enter your query:")

if st.button("Get Schedule"):
    if not user_input.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Generating your schedule..."):
            try:
                # Prepare the message
                messages = [
                    ChatMessage(role="user", content=user_input)
                ]
                
                # Get the response from MistralAI
                chat_response = client.chat(
                    model=model,
                    messages=messages,
                )
                
                # Display the response
                response = chat_response.choices[0].message.content
                st.write("### Suggested Schedule:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
