#!/usr/bin/env python

import webbrowser
import os
import time

url = 'https://onlyfans.com/?ref=13582078'

def repeat():
    tor_path = \
        'C:\\Users\\etern\\OneDrive\\Desktop\\Tor Browser\\Browser\\firefox.exe'
    webbrowser.register('tor', None, webbrowser.BackgroundBrowser(tor_path))
    webbrowser.get('tor').open(url)
    time.sleep(15)
    os.system("taskkill /im tor.exe /f")

while True:
    repeat()
