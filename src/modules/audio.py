import speech_recognition as sr
from datetime import datetime
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning master")
    elif hour>=12 and hour<17:
        speak("Good afternoon master")
    elif hour>=17 and hour<19:
        speak("Good evening master")
    else:
        speak("Good night master")

def aboutMe():
    speak("naan thaan TEREX")
    speak("what help do you want") 

def listenInput():
    r=sr.Recognizer()
  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        # r.energy_threshold()
        print("say anything : ")
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(query)
        except:
            print("sorry, could not recognise")
            mycommand()
        return query   