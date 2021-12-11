import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        
        if hour>=0 and hour<12:
                speak("Good Morning!")

        elif hour>=12 and hour<18:
                speak("Good Evening!")

        else:
                speak("Good Evening!")

        speak("I am Pika Sir.Please tell me how may I help you")

def takeCammand():
       

        r=sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio=r.listen(source)
        try:
                print("Recognizing...")
                query = r.recognize_google(audio,language='en-in')
                print(f"user said:{query}\n")

        except Exception as e:
                print(e)

                print("Say that again please...")
                return "None"

        return query

def sendEmail(to,content):
  server =smtplib.SMTP('smntp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login('youremail.com','your_password')
  server.sendmail('youremail@gmail.com',to,content)
  server.close()

wishMe()
# while True:
if 1:
    query=takeCammand().lower()

    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("search Wikipedia...")
        query=query.replace("wikipedia","")
        results =wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")

    elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
            music_dir='E:\\songs\\j'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    
    
    elif 'email to drake' in query:
            try:
                speak("What should I say?")
                content = takeCammand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 