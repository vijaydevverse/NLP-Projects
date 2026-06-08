import streamlit as st
from pdf_reader import extract_text
from summarizer import summarize

st.set_page_config(page_title="AI PDF Summarizer", layout="wide")

st.title("📄 AI PDF Summarizer (Exam + Work Notes)")

st.set_page_config(page_title="Fast PDF AI", layout="wide")

pdf_file = st.file_uploader("Upload your PDF file")

if pdf_file:
    text = extract_text(pdf_file)

    with st.spinner("Summarizing instantly..."):
        summary = summarize(text)

    st.subheader("📌 Summary")
    st.write(summary)