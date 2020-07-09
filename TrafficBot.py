import webbrowser
import os
import time

url = '<url to visit>'

tor_path="<path to Tor Browser>"
webbrowser.register('tor', None, webbrowser.BackgroundBrowser(tor_path))
webbrowser.get('tor').open(url)
time.sleep(15)
os.system("taskkill /im tor.exe /f")
webbrowser.get('tor').open(url)
os.system("taskkill /im tor.exe /f")
