import speech_recognition as sr
import pyttsx3
import torch

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            print(audio)
            text = recognizer.recognize_whisper(audio, language='spanish')
            text = text.lower()

            print(f"Recognized {text}")
    except sr.UnknownValueError():
        print('Unrecognized')
        recognizer = sr.Recognizer()
        continue
