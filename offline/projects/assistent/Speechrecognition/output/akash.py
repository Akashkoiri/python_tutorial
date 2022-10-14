import pyttsx3

engine = pyttsx3.init()

def settings():
    # print(voices[0].id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)

def speak(str):
    settings()
    engine.say(str)
    engine.runAndWait()
