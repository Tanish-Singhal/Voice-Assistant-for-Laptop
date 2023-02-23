import pyttsx3
import datetime
import speech_recognition as sr     # here we use aliasing
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')          # It was a Microsoft API 
voices = engine.getProperty('voices')   # getting details of current voices
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()     #without this command, speech will not be audible to us


print("\n")


def wishMe():       # this function wishme accordin to the time which was displayed by my system
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


        print("\n")


def takeCommand():          # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 1           #After every sentence it wait for 1 sec
        # r.energy_threshold = 300        #If threshold id low then it can also detect the background noise 
        audio = r.listen(source,0,4)      #It can wait for 4 sec for your response

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')     # Using google for voice recognition
        print(f"User said: {query}\n")      # User query will be printed

    except Exception as e:  
        print("Say that again please...")       # Say that again please... line will be printes in case of improper voice
        return "None"       # None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()       # Converting user query into lower case

        
        # Logic for executing tasks based on query
        if "aur batao kaise ho" in query:               # Here I also inlcude be=unch of Hindi commands which you can also use
            print ("Hum Bhaut Badiya hai, Ap Batao")
            speak ("Hum Bhaut Badiya hai, Ap Batao")


        elif "teacher se milo" in query:
            print ("Namaste Maam. Namaste Sir")
            speak ("Namaste Maam. Namaste Sir")

        
        elif "ek kam karo" in query:
            print ("Haa Batao")
            speak ("Haa Batao")
            
            
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("on wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            # quit()


        elif "open instagram" in query:
            webbrowser.open_new_tab("instagram.com")
            speak("Done sir!")
            # quit()


        elif "open whatsapp" in query:
            webbrowser.open_new_tab("web.whatsapp.com")
            speak("Done sir!")
            # quit()

        
        elif "open facebook" in query:
            webbrowser.open_new_tab("facebook.com")
            speak("Done sir!")
            # quit()


        elif "open youtube" in query:
            webbrowser.open_new_tab("youtube.com")
            speak("Done sir!")
            # quit()

            
        elif "search on youtube" in query:
            speak("What should I search for you sir ?")
            search = takeCommand()
            print(search)
            url = "https://www.youtube.com/results?search_query=" + search
            webbrowser.open(url)
            speak("Done sir!")
            # quit()


        elif "search on browser" in query:
            speak("What should I search for you sir ?")
            search = takeCommand()
            webbrowser.open_new_tab(search + "")
            speak("Done sir!")
            # quit()


        elif "open a website" in query:
            speak("Which website you want me to open sir ?")
            search = takeCommand()
            web = "https://www." + search + ".com"
            webbrowser.open(web)
            speak("Done sir!")
            # quit()


        elif "gana chalao" in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            # quit()

        
        elif "open new code file" in query:
            codepath = "C:\\Users\\Tanish Singhal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Done sir!")
            # quit()


        elif "microsoft excel chalao" in query:
            loc1 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(loc1)
            speak("Done sir!")
            # quit()


        elif "microsoft excel chalao" in query:
            loc2 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(loc2)
            speak("Done sir!")
            # quit()


        elif "microsoft excel chalao" in query:
            loc3 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(loc3)
            speak("Done sir!")
            # quit()


        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is ")
            print(strTime) 
            speak(strTime)
            # quit()
      

        elif "go to sleep mode" in query:
            speak("Ok sir, But you can call me anytime")
            # quit()


        else:
            speak("Try Again")
    
quit()
