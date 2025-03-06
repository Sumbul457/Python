import speech_recognition as sr
import webbrowser
import pyttsx3
import Musiclibrary
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()  # speech to text
engine = pyttsx3.init()  # text to speech
newsapi = "c372b36da80549eda78dad40111bebc7"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text): # this whole programme is taken the def function speak for accuracy
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 
    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):  
        words = c.lower().split(" ")
        if len(words) > 1:
            song = words[1]
            if song in Musiclibrary.music:
                webbrowser.open(Musiclibrary.music[song])
            else:
                speak_old("Song not found.")
        else:
            speak_old("Please specify a song name.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json() # API into pyhton dictonary
            articles = data.get('articles', [])
            for article in articles[:5]: # [:5] we add this to give few headlines not to put load on cpu
                speak_old(article['title'])


if __name__ == "__main__": # run the script first at all
    speak_old("Initializing Jarvis.......")

    while True:
        print("Recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
#             recognizer.recognize_google(audio) sends the audio to Google’s servers.
#             Google's AI processes the speech and returns the recognized text.

            if word.lower() == "jarvis":
                speak_old("Yes Mam")

                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")


"""Explaination"""

"""Modules"""

# import speech_recognition as sr 
# Listens to the user's voice input and converts it into text.

# import webbrowser
# to open websites

# import pyttsx3
# Offline text-to-speech engine

# import requests
# handles all type of API

# from gtts import gTTS
# to make sound more relaiable

# import pygame
# to make mp3 work and we use mp3 to make gtts work

# import os
# use to manage files and directory

"""Music play"""

# c = "Play Despacito"
# words = c.lower().split(" ")
# print(words)  # Output: ['play', 'despacito']
# song = words[1]  # "despacito"

