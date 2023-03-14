import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening....")
    audio = recognizer.listen(source)

    try:
        print("You said: " + recognizer.recognize_google(audio, language='es-MX'))
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as re:
        print(f'{re}')
