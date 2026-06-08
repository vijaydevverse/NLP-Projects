def detect_emotion(text):

    text = text.lower()

    happy_words = [
        "happy",
        "great",
        "awesome",
        "good",
        "love"
    ]

    sad_words = [
        "sad",
        "cry",
        "depressed"
    ]

    angry_words = [
        "angry",
        "mad",
        "hate"
    ]

    for word in happy_words:

        if word in text:

            return "Joy 😀"

    for word in sad_words:

        if word in text:

            return "Sadness 😢"

    for word in angry_words:

        if word in text:

            return "Anger 😡"

    return "Neutral 😐"