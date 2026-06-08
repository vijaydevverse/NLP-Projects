import PyPDF2
import streamlit as st

@st.cache_data
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()