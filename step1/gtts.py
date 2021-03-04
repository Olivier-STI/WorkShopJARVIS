#!/bin/python3 

import os
import gtts
from gtts import gtts

def hello():
    tts = gtts("hello world", lang='en')
    tts.save("hello.mp3")
    playsound.playSound("Hello.mp3")

hello()