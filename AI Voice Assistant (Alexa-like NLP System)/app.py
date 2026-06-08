from speech import speak
from listen import listen
from brain import process

speak("AI assistant activated")

while True:
    query = listen()

    if "exit" in query or "stop" in query:
        speak("Goodbye!")
        break

    process(query)