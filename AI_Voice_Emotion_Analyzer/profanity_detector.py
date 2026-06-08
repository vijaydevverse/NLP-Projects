def check_profanity(text):

    text = text.lower()

    bad_words = [
        "idiot",
        "stupid",
        "damn"
    ]

    for word in bad_words:

        if word in text:

            return "⚠️ Bad Word Detected"

    return "✅ Clean Language"