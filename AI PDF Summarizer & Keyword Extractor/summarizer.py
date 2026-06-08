import streamlit as st
import re
from collections import Counter

@st.cache_data
def summarize(text, max_sentences=5):

    # split sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # word frequency
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    # score sentences
    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    # get top sentences
    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    return " ".join(ranked[:max_sentences])