import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')          
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("\n")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Tanish")
        speak("Good Morning! Tanish")
       
    elif hour>=12 and hour<18:
        print("Good Afternoon! Tanish")
        speak("Good Afternoon! Tanish")
           
    else:
        print("Good Evening! Tanish")
        speak("Good Evening! Tanish")
        

    print("Zira is at your Service sir!")
    speak("Zira is at your Service sir!")

    print("Please Tell me how may I help you.....")
    speak("Please tell me how may I help you.....")    

