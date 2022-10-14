import Speech_recognition as sr

r = sr.Recognizer()

file = '\\audio\\audio.wav'

with sr.AudioFile(file) as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(f"You said: {text}")
