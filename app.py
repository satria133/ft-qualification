import os
import streamlit as st
import openai

# Set the title of the app
st.title("OpenAI API Key Example")

# Load the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found! Ensure it is set in your environment variables.")
else:
    st.success("API key loaded successfully!")

    # Example OpenAI API usage
    st.write("Testing the OpenAI API...")
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Say hello to Streamlit!",
            max_tokens=5,
        )
        st.write("Response from OpenAI:", response.choices[0].text.strip())
    except Exception as e:
        st.error(f"Error connecting to OpenAI: {e}")
