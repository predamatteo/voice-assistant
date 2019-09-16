import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang = 'it')
    filename= 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try : 
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('exception: ' + str(e))

    return said


print('pronto')
text = get_audio()

if 'ciao' in text:
    speak('ciao')

if 'qual\'è il tuo nome' in text:
    speak('il mio nome è zoxi')
