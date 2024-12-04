import streamlit as st
import os
from mistralai import Mistral

# API Key and Model Setup
api_key = os.environ.get("MISTRAL_API_KEY")
if not api_key:
    st.error("API key is not set. Please configure the MISTRAL_API_KEY environment variable.")
else:
    client = Mistral(api_key=api_key)
    model = "mistral-large-latest"

# Streamlit UI
st.title("Schedule Assistant")
st.write("Get a schedule to manage effectively.")

# User Input
user_input = st.text_input("Enter your query:")

if st.button("Get Schedule"):
    if not user_input.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Generating your schedule..."):
            try:
                # Get the response from Mistral
                chat_response = client.chat.complete(
                    model=model,
                    messages=[
                        {"role": "user", "content": user_input},
                    ]
                )
                
                # Extract and display the response
                response = chat_response.choices[0].message.content
                st.write("### Suggested Schedule:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
