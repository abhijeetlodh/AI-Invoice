import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Configure the Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to read all text from files in a directory
def read_files_from_directory(directory):
    text_data = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.txt', '.pdf')):  # Adjust extensions as needed
                file_path = os.path.join(root, file)
                if file.endswith('.txt'):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text_data += f.read() + "\n"
                elif file.endswith('.pdf'):
                    reader = PdfReader(file_path)
                    for page in reader.pages:
                        text_data += page.extract_text() + "\n"
    return text_data

# Load text data from the specified directory
directory_path = '/workspaces/AI-Invoice/Test_Data-Zolvit/test data'
text_data = read_files_from_directory(directory_path)

# Function to get response from Google Generative AI
def get_gemini_response(input_text, context):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, context])
    return response.text

# Streamlit UI
st.title("Data Extraction")

# User input
user_input = st.text_input("Ask your question:")

if st.button("Submit"):
    if user_input:
        # Generate a response using the Google Generative AI model
        response_text = get_gemini_response(user_input, text_data)
        st.write(response_text)
    else:
        st.warning("Please enter a question.")
