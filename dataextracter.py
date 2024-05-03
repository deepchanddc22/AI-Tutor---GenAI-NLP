import streamlit as st
import os
import google.generativeai as genai
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="gemini-pro")



def get_question(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content('''generate atleast ten mcq questions with atleast 4 non null options on''' + text + ''' with question,information,options,answer. provide the response as a json [
    {
        "question": "What is the primary goal of artificial intelligence?",
        "information": "This field of computer science aims to create systems capable of performing tasks that would typically require human intelligence.",
        "options": ["To simulate human intelligence", "To enhance computer speed", "To replace human jobs", "To improve data storage"],
        "answer": "To simulate human intelligence"
    },
    {
        "question": "What is 'machine learning' in the context of artificial intelligence?",
        "information": "This is a subset of artificial intelligence that involves the creation of systems that can learn from and make decisions based on data.",
        "options": ["A new programming language", "A data processing method", "A subset of artificial intelligence", "A type of computer hardware"],
        "answer": "A subset of artificial intelligence"
    }''', generation_config=genai.types.GenerationConfig(temperature=0.5))
    
    print(response.text)
    filename = "quiz_data.json"

    # Convert the text to a dictionary
    data = json.loads(response.text)

    # Save data to a JSON file
    with open(filename, "w") as json_file:
         json.dump(data, json_file, indent=2)
    
    st.write("Processing completed. MCQ questions have been generated.")


st.title("AI Tutor 🤖")
st.header("Upload Your Material To Get Tested")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    # Read PDF
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    get_question(text)
