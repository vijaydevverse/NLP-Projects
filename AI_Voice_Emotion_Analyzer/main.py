from speech_to_text import get_speech
from language_detector import detect_language
from sentiment_analyzer import analyze_sentiment
from emotion_detector import detect_emotion
from profanity_detector import check_profanity
from translator import translate_to_english

print("\n===================================")
print(" AI Voice Emotion Analyzer ")
print("===================================\n")

text = get_speech()

print("\n📝 Spoken Text:")
print(text)

language = detect_language(text)
meaning = translate_to_english(text)

print("\n🌐 Language:")
print(language)

print("\n📖 English Meaning:")
print(meaning)

sentiment = analyze_sentiment(text)

print("\n📊 Sentiment:")
print(sentiment)

emotion = detect_emotion(text)

print("\n😀 Emotion:")
print(emotion)

profanity = check_profanity(text)

print("\n🚫 Profanity Check:")
print(profanity)

print("\n✅ Analysis Complete")