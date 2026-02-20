import swisseph as swe
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime, date
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import pygame
import time
import psutil


# ---------------- YOUR BIRTH DETAILS ----------------
# ✏️ CHANGE THESE ONLY ONCE

year = 2006
month = 1
day = 11
hour = 11
minute = 55
city = "bhavnagar"


# ---------------- EPHEMERIS ----------------
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_LAHIRI)


# ---------------- WAIT 5 MIN AFTER START ----------------
def wait_after_startup():

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()

    diff = (now - boot_time).total_seconds()
    wait_time = 300   # 5 minutes

    if diff < wait_time:
        remaining = wait_time - diff
        print(f"Waiting {int(remaining)} sec...")
        time.sleep(remaining)


# ---------------- ONCE PER DAY ----------------
def can_play_today():

    file = "last_played.txt"
    today = str(date.today())

    if os.path.exists(file):
        with open(file, "r") as f:
            if f.read() == today:
                print("Already played today.")
                return False

    with open(file, "w") as f:
        f.write(today)

    return True


# ---------------- LOCATION ----------------
def get_lat_long(city):

    geo = Nominatim(user_agent="astro_app")
    loc = geo.geocode(city)

    if loc:
        return loc.latitude, loc.longitude
    else:
        return None, None


# ---------------- TIMEZONE ----------------
def get_timezone(lat, lon):

    tf = TimezoneFinder()
    return tf.timezone_at(lat=lat, lng=lon)


# ---------------- RASHI ----------------
def get_chandra_rashi(y, m, d, h, mi, lat, lon):

    tz_name = get_timezone(lat, lon)
    tz = pytz.timezone(tz_name)

    local = tz.localize(datetime(y, m, d, h, mi))
    utc = local.astimezone(pytz.utc)

    jd = swe.julday(
        utc.year,
        utc.month,
        utc.day,
        utc.hour + utc.minute/60
    )

    moon = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
    index = int(moon / 30)

    rashis = [
        "Mesh", "Vrishabh", "Mithun", "Kark",
        "Singh", "Kanya", "Tula", "Vrischik",
        "Dhanu", "Makar", "Kumbh", "Meen"
    ]

    return rashis[index]


# ================= PROGRAM START =================

wait_after_startup()

if not can_play_today():
    exit()


lat, lon = get_lat_long(city)

if not lat:
    print("City not found.")
    exit()

rashi = get_chandra_rashi(
    year, month, day,
    hour, minute,
    lat, lon
)

print("Your Rashi:", rashi)


# ---------------- URL ----------------
urls = {
    "Mesh": "https://www.divyabhaskar.co.in/rashifal/13/today/",
    "Vrishabh": "https://www.divyabhaskar.co.in/rashifal/15/today/",
    "Mithun": "https://www.divyabhaskar.co.in/rashifal/16/today/",
    "Kark": "https://www.divyabhaskar.co.in/rashifal/17/today/",
    "Singh": "https://www.divyabhaskar.co.in/rashifal/18/today/",
    "Kanya": "https://www.divyabhaskar.co.in/rashifal/19/today/",
    "Tula": "https://www.divyabhaskar.co.in/rashifal/20/today/",
    "Vrischik": "https://www.divyabhaskar.co.in/rashifal/14/today/",
    "Dhanu": "https://www.divyabhaskar.co.in/rashifal/21/today/",
    "Makar": "https://www.divyabhaskar.co.in/rashifal/22/today/",
    "Kumbh": "https://www.divyabhaskar.co.in/rashifal/23/today/",
    "Meen": "https://www.divyabhaskar.co.in/rashifal/24/today/"
}

url = urls.get(rashi)

if not url:
    print("URL not found.")
    exit()


# ---------------- SCRAP ----------------
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

content = soup.find("p")

if not content:
    print("Content not found.")
    exit()

text = content.text.strip()

print("\nBhavishya:\n", text)


# ---------------- TTS ----------------
tts = gTTS(text=text, lang="gu")
tts.save("rashi.mp3")


# ---------------- AUDIO ----------------
pygame.mixer.init()
pygame.mixer.music.load("rashi.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Finished.")