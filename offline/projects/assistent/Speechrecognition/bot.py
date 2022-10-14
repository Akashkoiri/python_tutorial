import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listning")
        # r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing")
        text = r.recognize_google(audio)
    return text
    
def speak(str):
    # print(voices[0].id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)

    engine.say(str)
    engine.runAndWait()

speak("Helloo gooood")
# speak('Hello bro!,How are you?')