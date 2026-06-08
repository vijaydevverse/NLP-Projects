import webbrowser
import datetime
import wikipedia
from speech import speak

def process(query):

    if "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    else:
        speak("I am still learning this command")