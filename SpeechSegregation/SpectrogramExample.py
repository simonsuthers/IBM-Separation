# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:28:56 2018

@author: User
"""

#%% Microsoft speech engine

import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Hello")


#%% https://www.ibm.com/watson/developercloud/text-to-speech/api/v1/python.html?python#authentication
from tts_watson.TtsWatson import TtsWatson


