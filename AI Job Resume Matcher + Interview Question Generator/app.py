import streamlit as st
from resume_reader import extract_text
from matcher import match
from question_generator import generate_questions

st.title("AI Resume Matcher + Interview Generator")

resume_file = st.file_uploader("Upload Resume PDF")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:

    with st.spinner("Reading resume..."):
        resume_text = extract_text(resume_file)

    with st.spinner("Analyzing match..."):
        score = match(resume_text, job_desc)

    st.subheader(f"Match Score: {score}%")

    if score < 50:
        st.warning("Low match - improve skills")
    elif score < 75:
        st.info("Good match - some improvements needed")
    else:
        st.success("Excellent match!")

    st.subheader("📌 Interview Questions")
    questions = generate_questions(resume_text, job_desc)

    for q in questions:
        st.write("• " + q)