import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

recognizer = sr.Recognizer()
translator = Translator()

meeting_notes = []

print("=== AI Meeting Translator ===")
print("Say 'stop meeting' to finish.\n")

while True:

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")

        try:

            audio = recognizer.listen(source)

            english_text = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("Speaker:", english_text)

            if "stop meeting" in english_text.lower():
                break

            meeting_notes.append(english_text)

            translated = translator.translate(
                english_text,
                dest="hi"
            )

            hindi_text = translated.text

            print("Hindi:", hindi_text)

            tts = gTTS(
                text=hindi_text,
                lang="hi"
            )

            tts.save("temp.mp3")

            os.system("start temp.mp3")

        except Exception as e:
            print(e)

print("\nMeeting Ended")

with open("meeting_notes.txt", "w", encoding="utf-8") as file:
    for note in meeting_notes:
        file.write(note + "\n")

print("Notes Saved")