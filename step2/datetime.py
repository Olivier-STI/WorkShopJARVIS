#!/bin/python3 

import os
import gtts
import datetime

def date():
    date = datetime.date()
    tts = gtts(data, lang='en')
    tts.save("Date.mp3")
    playsound.playSound("Date.mp3")

date()