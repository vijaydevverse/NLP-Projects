from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

with open(
        "meeting_notes.txt",
        "r",
        encoding="utf-8"
) as file:

    text = file.read()

summary = summarizer(
    text,
    max_length=150,
    min_length=50,
    do_sample=False
)

print(summary[0]["summary_text"])