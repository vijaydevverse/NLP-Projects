import re

def extract_section(text, keywords):
    for kw in keywords:
        if kw in text.lower():
            return True
    return False


def generate_questions(resume_text, job_desc):

    text = (resume_text + " " + job_desc).lower()

    questions = []

    # -----------------------
    # 🧰 TOOLS / SKILLS
    # -----------------------
    tools_keywords = ["python", "java", "sql", "excel", "power bi", "tableau",
                      "machine learning", "deep learning", "nlp", "aws"]

    for tool in tools_keywords:
        if tool in text:
            questions.append(f"How did you use {tool} in your projects or work experience?")

    # -----------------------
    # 💼 EXPERIENCE / INTERNSHIP
    # -----------------------
    if any(word in text for word in ["intern", "internship", "experience", "worked"]):
        questions.append("Explain your internship or work experience in detail.")
        questions.append("What was your role and responsibilities in your previous work?")

    # -----------------------
    # 🎯 PROJECTS
    # -----------------------
    if "project" in text:
        questions.append("Tell me about your most impactful project.")
        questions.append("What challenges did you face in your project and how did you solve them?")

    # -----------------------
    # 🎮 HOBBIES
    # -----------------------
    if any(word in text for word in ["hobby", "hobbies", "sports", "music", "reading"]):
        questions.append("How do your hobbies help you improve your professional skills?")

    # -----------------------
    # 🔥 COMMON HR QUESTIONS
    # -----------------------
    questions.append("Why should we hire you for this role?")
    questions.append("Where do you see yourself in the next 5 years?")
    questions.append("What are your strengths and weaknesses?")

    return questions[:10]  # limit output