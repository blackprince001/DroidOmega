import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random

from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            apollo_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        
        #Errot Handling
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            apollo_speak('Sorry, I did not get That')
        except sr.RequestError:
            apollo_speak('Sorry, my speech service is down')
        return voice_data

def apollo_speak(audio_string):
    
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    
    playsound.playsound(audio_file)
    
    print(audio_string)
    
    os.remove(audio_file)

def respond(voice_data):
    # feel free to add more data bits to this function
    
    if 'what is your name' in voice_data:
        apollo_speak("I am Apollo, Let me Light up your way.")
        
    if 'what time is it' in voice_data:
        apollo_speak(ctime())
        
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        apollo_speak("This is what i found for you --" + search)
        
    if 'find location' in voice_data:
        location = record_audio()
        url = 'https://www.google.nl/maps/place/' + location + '/%amp;'
        webbrowser.get().open(url)
        apollo_speak('here Is your location' + search)
        
# use when you want to exit loop or code becomes a nuisance        
    if 'exit' in voice_data:
        exit()


time.sleep(1)
print("Welcome, I am Apollo, Greek God of Photons.")

while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
