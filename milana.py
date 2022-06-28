import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'milana' in command:
                command = command.replace('milana', '')
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi!')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'exit' in command:
        talk("Ok")
        exit()
    elif 'uganda' in command:
        webbrowser.open("https://www.youtube.com/watch?v=1JABdS-HN5A")
    elif 'rick astley' in command:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif 'rick roll' in command:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif 'never gonna give you up' in command:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        talk('Please say the command again.')
        

while True:
    run_alexa()
