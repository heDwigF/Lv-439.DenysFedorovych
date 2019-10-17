import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
# from fuzzywuzzy import fuzz
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('6U77EK-R4PEWA3848')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """This function let you speak """
    print('Virtual: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    """This function welcome you """
    current_time = int(datetime.datetime.now().hour)
    if current_time >= 0 and current_time < 12:
        speak('Good Morning!')

    if current_time >= 12 and current_time < 18:
        speak('Good Afternoon!')

    if current_time >= 18 and current_time !=0:
        speak('Good Evening!')

greeting()

speak('Hi, my name is Angela, I will be your personal assistant')
speak('How I can help you?')


def execution():
    """This function make main actions with volume """
   
    vol = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        vol.pause_threshold =  1
        audio = vol.listen(source)
    try:
        query = vol.recognize_google(audio, language= 'us')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry, I don\'t understand you. Try typing from the keyboard: ')
        query = str(input('Input by keyboard: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = execution()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('wait a minute')
            webbrowser.open('www.youtube.com')

        elif 'current time' in query:
            now = datetime.datetime.now()
            speak("Now " + str(now.hour) + ":" + str(now.minute))

        elif "what\'s up" in query or 'how are you' in query or 'How do you fell today' in query or 'how are you' in query:
            myMessages = ['All is OK', 'I am fine!', 'Nice!', 'I am ready to work', 'I am full of strength and ready to go. Thank you for your concern!']
            speak(random.choice(myMessages))       

        elif 'open google' in query:
            speak('wait a minute')
            webbrowser.open('www.google.com.ua')

        elif 'open gmail' in query:
            speak('wait a minute')
            webbrowser.open('www.gmail.com')
        
        elif 'music' in query:
            speak('wait a minute')
            os.system("F:\\badguy.mp3")

        elif 'exit' in query or 'denny' in query or 'stop' in query or 'nothing' in query or 'nothing' in query:
            speak('okay')
            speak('Good bye, dear User, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello, dear User')

        elif 'bye' in query:
            speak('Good bye, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('According to my knowledge base: ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('From Wikipedia: ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Say something...')