import requests
from bs4 import BeautifulSoup
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    print("\n🗣️ Speaking:", text)
    engine.say(text)
    engine.runAndWait()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_live_matches():
    try:
        url = "https://www.cricbuzz.com/cricket-match/live-scores/upcoming-matches"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Find live match containers — class names may change, inspect page
        live_sections = soup.find_all("div", class_="cb-lv-scrs-col text-black")  # example selector for score
        match_blocks = soup.find_all("div", class_="cb-lv-card")  # adjust after inspecting

        live_matches = []

        for block in match_blocks:
            try:
                teams = block.find("h3", class_="cb-lv-scr").get_text(strip=True)
                status = block.find("div", class_="cb-lv-status").get_text(strip=True)
                if "live" in status.lower() or "in progress" in status.lower():
                    live_matches.append(f"{teams} – {status}")
            except:
                continue

        if live_matches:
            for match in live_matches:
                speak(f"Live now: {match}")
            return True
        else:
            speak("No live cricket matches right now.")
            return False

    except Exception as e:
        print("Error:", str(e))
        speak("Sorry, could not fetch cricket data.")
        return False

if __name__ == "__main__":
    print("Starting Cricbuzz Live Speaker (scraping version)...")
    speak("Starting cricket live match speaker")

    while True:
        has_live = check_live_matches()
        print("\nWaiting 180 seconds...\n")
        time.sleep(10)