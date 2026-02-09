import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import pygame
import time

sign = input("enter your rashi :")

if sign == 'aries':
    url = "https://www.divyabhaskar.co.in/rashifal/13/today/"   # fake API for testing
elif sign == 'taurus':
    url = "https://www.divyabhaskar.co.in/rashifal/15/today/"
elif sign == 'gemini':
    url = "https://www.divyabhaskar.co.in/rashifal/16/today/"
elif sign == 'cancer':
    url = "https://www.divyabhaskar.co.in/rashifal/19/today/"
elif sign == 'leo':
    url = "https://www.divyabhaskar.co.in/rashifal/17/today/"
elif sign == 'virgo':
    url = "https://www.divyabhaskar.co.in/rashifal/18/today/"
elif sign == 'libra':
    url = "https://www.divyabhaskar.co.in/rashifal/20/today/"
elif sign == 'scorpio':
    url = "https://www.divyabhaskar.co.in/rashifal/14/today/"
elif sign == 'sagittarius':
    url = "https://www.divyabhaskar.co.in/rashifal/21/today/"
elif sign == 'capricorn':
    url = "https://www.divyabhaskar.co.in/rashifal/22/today/"
elif sign == 'aquarius':
    url = "https://www.divyabhaskar.co.in/rashifal/23/today/"
elif sign == 'pisces':
    url = "https://www.divyabhaskar.co.in/rashifal/24/today/"
else:
    print("invalid rashi")


# Example: Fetch data from a public test API
url = "https://www.divyabhaskar.co.in/rashifal/13/today?ref=inbound_RHS"   # fake API for testing
try:
    response = requests.get(url, timeout=10)           # timeout prevents hanging forever
    # Check if request was successful (status 200 = OK)
    if response.status_code == 200:
        #store response in variable
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        # print(soup.title.text)
        content = soup.find("div",class_='a6b3d8fe')
        #convert it into text to speech
        # print(content)
        tts = gTTS(text=content.text, lang='gu', slow=False)  # slow=True for slower/clearer speech
        tts.save("1.mp3")
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

        pygame.mixer.music.load('1.mp3')   # or .wav / .ogg
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play()             # loop forever (remove -1 to play once)

        print("Playing... press Ctrl+C to stop")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
        print("Stopped")
    else:
        print(f"Error: Server returned {response.status_code}")
        print(response.text)                           # see error message from server

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
