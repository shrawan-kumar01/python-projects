'''
Whatsup automation 
'''
#  import liberies 
import time 
time.sleep(120) # programm will start after two mint ,after the time of pc start

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
from plyer import notification

#  inporting all modules is completed  by here 

#  creating function for message under try

def message():
    try:
        url ="https://web.whatsapp.com/send?phone=+918860803188"

        message = "good morning" 
        path =""


    except Exception as e:
        pass