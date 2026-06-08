from langdetect import detect

def detect_language(text):

    text = text.lower()

    hindi_words = [
        "mera","maine","aaj","bahut",
        "khush","hun","hai","naam"
    ]

    tamil_words = [
        "en","peyar","naan",
        "vanakkam"
    ]

    malayalam_words = [
        "ente","peru","anu"
    ]

    telugu_words = [
        "naa","peru","nenu"
    ]

    kannada_words = [
        "nanna","hesaru","naanu"
    ]

    french_words = [
        "bonjour",
        "merci",
        "je",
        "suis",
        "heureux",
        "comment",
        "allez",
        "vous",
        "m'appelle"
    ]

    for word in hindi_words:
        if word in text:
            return "Hindi"

    for word in tamil_words:
        if word in text:
            return "Tamil"

    for word in malayalam_words:
        if word in text:
            return "Malayalam"

    for word in telugu_words:
        if word in text:
            return "Telugu"

    for word in kannada_words:
        if word in text:
            return "Kannada"

    for word in french_words:
        if word in text:
            return "French"

    try:

        code = detect(text)

        languages = {
            "en": "English",
            "fr": "French",
            "de": "German",
            "es": "Spanish",
            "ar": "Arabic",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "ja": "Japanese",
            "ko": "Korean",
            "zh-cn": "Chinese"
        }

        return languages.get(code, code)

    except:
        return "Unknown"