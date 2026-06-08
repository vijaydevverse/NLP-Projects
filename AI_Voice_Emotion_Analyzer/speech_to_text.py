import speech_recognition as sr

def get_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Speak Something...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

        try:

            # Supports English + Indian Languages
            text = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            return text

        except sr.UnknownValueError:

            return "Could not understand speech"

        except sr.RequestError:

            return "Internet Error"


if __name__ == "__main__":

    print(get_speech())