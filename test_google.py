import speech_recognition as sr
from threading import Thread
from queue import Queue

recognizer = sr.Recognizer()
recording = Queue()
messages = Queue()

messages.put(True)


def record_microphone():
    while not messages.empty():
        with sr.Microphone(sample_rate=16000) as source:
            print("Listening....")
            audio = recognizer.listen(source)
            recording.put(audio)


def speech_recognition_google():
    while not messages.empty():
        audio = recording.get()

        try:
            print("You said: " + recognizer.recognize_google(audio, language='es-MX'))
        except sr.UnknownValueError:
            print("Couldn't understand")
        except sr.RequestError as re:
            print(f'{re}')


print("Starting")
record = Thread(target=record_microphone)
record.start()

recognize = Thread(target=speech_recognition_google)
recognize.start()
