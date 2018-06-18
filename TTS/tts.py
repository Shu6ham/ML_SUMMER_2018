#!/usr/bin/python3

from gtts import gTTS
import os

text_input=input('Enter the text: ')
#print(text_input)
tts=gTTS(text=text_input,lang='hi')
tts.save('welcome.mp3')
os.system('vlc welcome.mp3')
