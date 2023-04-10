import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import psutil
import speedtest
import winsound


 
engine = pyttsx3.init('sapi5') #use to take inbuilt voices
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[1].id)




def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodMorning!")

    elif hour>=12 and hour<18:
        speak("good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir Please tell me how may i help you")

def takeCommand():
    #It takes micro phone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recogniing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
            
        print("Say that again please...")
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    print(f"Done,alarm is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ == "__main__":
    wishMe()
    #alarm('2:40 AM')
    while True:
        query=takeCommand().lower()

#logic on exsiquiting tasks based on query
        
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")



        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")


        elif 'open code' in query:
           codePath = "C:\\Users\\SURAVI\\AppData\\Local\\Programs\\Microsoft VS Code\ \Code.exe"
           os.startfile(codePath)

        elif 'email to suravi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "suravi08.mitra@gmail.com"
                sendemail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
            speak("Sorry my friend suravi.I am not able to send this email at this moment")
                

        elif "tempreature" in query:

            search = "tempreature in bhubaneshwar"
            url = f"https://www.google.com//search?q={search}"
            r = request.get(url)
            data = BeautifulSoup(r.tedxt,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")


        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
        

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up=st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second downloading speed")


        elif 'alarm' in query:
            speak("sir please tell me the time to set alarm.for example, set alarm at 2:30am")
            tt = takecommand()
            tt = tt.replace("set alarm to","")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)
