import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Initialize MistralAI client
api_key = "wEV53a5YgYXiN6TXZchorjpVwr1zsMHp"
model = "mistral-large-latest"
client = MistralClient(api_key=api_key)

# Streamlit UI
st.title("Schedule Assistant")
st.write("Get a schedule to manage effectively.")

# User input
user_input = st.text_input("Enter your query:")

if st.button("Get Schedule"):
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

