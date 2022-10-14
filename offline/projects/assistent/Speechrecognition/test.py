import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
        print("Listning")
        # r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing")
        text = r.recognize_google(audio)
        print(text)