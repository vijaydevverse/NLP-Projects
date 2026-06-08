import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

@st.cache_data
def extract_keywords(text, n=10):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out()
    scores = X.toarray()[0]

    ranked = sorted(zip(keywords, scores), key=lambda x: x[1], reverse=True)

    return [word for word, score in ranked[:n]]