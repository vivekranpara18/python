import swisseph as swe
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import pygame
import time


# Set ephemeris
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_LAHIRI)


# -------- Get Lat/Long from City --------
def get_lat_long(city):
    geolocator = Nominatim(user_agent="astro_app")
    location = geolocator.geocode(city)

    if location:
        return location.latitude, location.longitude
    else:
        print("City not found!")
        return None, None


# -------- Get Timezone from Lat/Long --------
def get_timezone(lat, lon):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    return timezone_str


# -------- Chandra Rashi --------
def get_chandra_rashi(year, month, day, hour, minute, lat, lon):

    # Find timezone
    tz_name = get_timezone(lat, lon)
    tz = pytz.timezone(tz_name)

    # Local datetime
    local_time = tz.localize(datetime(year, month, day, hour, minute))

    # Convert to UTC
    utc_time = local_time.astimezone(pytz.utc)

    # Decimal UTC hour
    time_decimal = utc_time.hour + utc_time.minute / 60.0

    # Julian Day
    jd = swe.julday(
        utc_time.year,
        utc_time.month,
        utc_time.day,
        time_decimal
    )

    # Moon position (Sidereal)
    moon_pos = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0]
    moon_longitude = moon_pos[0]

    rashi_index = int(moon_longitude / 30)

    rashis = [
        "Mesh (Aries)",
        "Vrishabh (Taurus)",
        "Mithun (Gemini)",
        "Kark (Cancer)",
        "Singh (Leo)",
        "Kanya (Virgo)",
        "Tula (Libra)",
        "Vrischik (Scorpio)",
        "Dhanu (Sagittarius)",
        "Makar (Capricorn)",
        "Kumbh (Aquarius)",
        "Meen (Pisces)"
    ]

    return rashis[rashi_index], moon_longitude, tz_name


# -------- USER INPUT --------
year = int(input("Birth Year: "))
month = int(input("Birth Month: "))
day = int(input("Birth Day: "))
hour = int(input("Birth Hour (24h): "))
minute = int(input("Birth Minute: "))
city = input("Enter Birth City: ")


# -------- AUTO LOCATION --------
lat, lon = get_lat_long(city)

if lat and lon:

    print(f"\nLatitude: {lat}")
    print(f"Longitude: {lon}")

    rashi, degree, tz = get_chandra_rashi(
        year, month, day, hour, minute,
        lat, lon
    )

    print("Timezone Detected:", tz)
    print("Moon Degree:", degree)
    print("Your Chandra Rashi:", rashi)


if rashi=='Mesh (Aries)':
    url = "https://www.divyabhaskar.co.in/rashifal/13/today/"   # fake API for testing
elif rashi=='Vrishabh (Taurus)':
    url ="https://www.divyabhaskar.co.in/rashifal/15/today/"
elif rashi=='Mithun (Gemini)':
    url ="https://www.divyabhaskar.co.in/rashifal/16/today/"
elif rashi=='Kark (Cancer)':
    url ="https://www.divyabhaskar.co.in/rashifal/16/today/"
elif rashi=='Singh (Leo)':
    url ="https://www.divyabhaskar.co.in/rashifal/17/today/"
elif rashi=='Kanya (Virgo)':
    url ="https://www.divyabhaskar.co.in/rashifal/18/today/"
elif rashi=='Tula (Libra)':
    url ="https://www.divyabhaskar.co.in/rashifal/20/today/"
elif rashi=='Vrischik (Scorpio)':
    url ="https://www.divyabhaskar.co.in/rashifal/14/today/"
elif rashi=='Dhanu (Sagittarius)':
    url ="https://www.divyabhaskar.co.in/rashifal/21/today/"
elif rashi=='Makar (Capricorn)':
    url ="https://www.divyabhaskar.co.in/rashifal/22/today/"
elif rashi=='Kumbh (Aquarius)':
    url ="https://www.divyabhaskar.co.in/rashifal/23/today/"
elif rashi=='Meen (Pisces)':
    url ="https://www.divyabhaskar.co.in/rashifal/24/today/"
else:
    print("Enter envalid rashi")

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