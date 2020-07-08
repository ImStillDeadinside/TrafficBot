import webbrowser
import os
import time

url = 'https://github.com/ghsecurity/LinuxCheatSheet'

tor_path="C:\\Users\\etern\\OneDrive\\Desktop\\Tor Browser\\Browser\\firefox.exe"
webbrowser.register('tor', None, webbrowser.BackgroundBrowser(tor_path))
webbrowser.get('tor').open(url)
time.sleep(15)
os.system("taskkill /im tor.exe /f")
webbrowser.get('tor').open(url)
os.system("taskkill /im tor.exe /f")