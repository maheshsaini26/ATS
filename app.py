import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_prompt(resume_text):
    # Customize the prompt based on the resume content
    prompt = f"Generate as many technical questions based on the following resume and give answer also for that following question:\n{resume_text}"
    return prompt

# Streamlit app
st.title("Welcome to ATS Resume Breaker")

# Sidebar contents 
with st.sidebar:
    st.title('ATS Resume Breaker 💬') 
    st.markdown(''' About This app is an ATS Resume Breaker powered by Google Generative AI and Gemini.
    - Extracts insights from resumes in PDF format.
    - Uses Gemini language model for question-answering.
    - Enhance your hiring process with AI! ''')
 
# File upload and submit button
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        prompt = generate_prompt(resume_text)
        response = get_gemini_response(prompt)
        st.subheader("Generated Questions:")
        st.write(response)
