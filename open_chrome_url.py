import time

import speech_recognition as sr
import webbrowser as wb
import pyttsx3
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
python_path = 'C:/Users/DELL/AppData/Local/Programs/Python/Python36-32/python.exe %s'

r = sr.Recognizer()
r.energy_threshold = 4000
engine = pyttsx3.init()

with sr.Microphone() as source:
    print('Say Something!')
    engine.say('Hola! I would help you in redirecting you to the web page! Please give me the url')
    engine.runAndWait()
    audio = r.listen(source)
    print('Done!')

try:
    text = r.recognize_google(audio)
    print('You said:\n' + text)
    wb.get(chrome_path).open(text)
    print('Welcome to '+text)
    engine.say('Welcome to '+text)
    engine.runAndWait()

except Exception as e:
    print(e)

with sr.Microphone() as source:

    engine.say('DO YOU WANT TO REGISTER OR LOGIN')
    engine.runAndWait()
    audio = r.listen(source)
    print('Done!')

try:
    text = r.recognize_google(audio)
    print('You said:\n' + text)
    if(text=='register'):
     wb.get(python_path).open('datasetCreator.py')
     wb.get(python_path).open('trainner.py')
     engine.say('u r registered')
     engine.runAndWait()
    elif (text == 'login'):
        engine.say('i am going to capture you')
        engine.runAndWait()
        wb.get(python_path).open('detector.py')
        time.sleep(10)
        engine.say('you are logged in')
        engine.runAndWait()


except Exception as e:
    print(e)

