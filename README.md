# ATS Resume Breaker 🔍

An AI-powered application that analyzes resumes/CVs and generates technical interview questions using Google's Gemini Pro model. Built with Streamlit and Generative AI.

## Features ✨
- **PDF Resume Analysis**: Extracts text from uploaded PDF files
- **AI-Powered Q&A Generation**: Generates technical questions based on resume content
- **Streamlit Web Interface**: User-friendly GUI for easy interaction
- **Google Gemini Integration**: Leverages state-of-the-art language model
- **Environment Configuration**: Secure API key management using `.env`

## Installation 🛠️

### Prerequisites
- Python 3.8+
- Google API key with Gemini access
- pip package manager

### Setup
1. Clone the repository:
git clone https://github.com/your-username/ats-resume-breaker.git
cd ats-resume-breaker

2. Install dependencies:
pip install -r requirements.txt

3. Create .env file:
GOOGLE_API_KEY=your_api_key_here

Usage 🚀

1. Start the application:
streamlit run app.py

2. In the web interface:
Upload a PDF resume
Click "Submit"
View generated technical questions

3. Example output:
Generated Questions:
1. Explain your experience with Python-based web development...
2. Describe your approach to machine learning model deployment...
   
Configuration ⚙️:

Obtain Google API key from Google AI Studio

Add API key to .env file

Customize prompt engineering in generate_prompt() function

Dependencies 📦:

streamlit

google-generativeai

PyPDF2

python-dotenv

Tech Stack 💻:

Frontend: Streamlit

AI Backend: Google Gemini Pro

PDF Processing: PyPDF2

Configuration: python-dotenv

![app · Streamlit - Personal - Microsoft​ Edge 29-01-2025 19_15_32](https://github.com/user-attachments/assets/c292b6e0-d57d-46a1-ac44-19df2ced38d4)
