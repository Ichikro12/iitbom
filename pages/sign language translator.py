import streamlit as st
import subprocess

def run_sign_language_translator():
    """Function to call the sign_language_translator.py script."""
    # Replace 'sign_language_translator.py' with the actual filename
    command = ['python', 'C:/Users/ckp23\Videos/iitbombay-main/iitbombay-main/pythonProject1/pages/slang.py']
    subprocess.run(command)

# Title and description
st.title("Sign Language Translator")
st.write("Click the button below to start the sign language translator script.")

# Button to trigger script execution
if st.button("Start Translator"):
    run_sign_language_translator()
