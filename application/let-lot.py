# =====================================================================
# Find Latitude & Longitude from Birthplace Name using geopy (Nominatim)
# Great for Vedic astrology scripts (VedAstro, PyJHora, etc.)
# =====================================================================

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

def get_coordinates(place_name):
    """
    Get latitude and longitude from a place name using Nominatim (OpenStreetMap).
    Returns (lat, lon, full_address) or (None, None, None) if not found.
    """
    # Important: Nominatim requires a user_agent (your app/email)
    # Change "your_name_or_app" to something real (helps them contact you if needed)
    geolocator = Nominatim(user_agent="my_astrology_script_vivek_2025")
    
    # Rate limiting: Nominatim policy = max 1 request per second
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.1)
    
    try:
        print(f"\nSearching for: {place_name} ...")
        location = geocode(place_name)
        
        if location is not None:
            return (
                round(location.latitude, 6),   # precision good for astrology
                round(location.longitude, 6),
                location.address
            )
        else:
            print("→ No location found.")
            return None, None, None
            
    except Exception as e:
        print(f"Error during geocoding: {e}")
        return None, None, None


# ==================== MAIN PROGRAM ====================
print("🌍 Birthplace to Latitude/Longitude Finder (using geopy) 🌍\n")

while True:
    place = input("Enter birth place (e.g. Ahmedabad, Gujarat, India): ").strip()
    
    if not place:
        print("Please enter a place name.")
        continue
    
    lat, lon, address = get_coordinates(place)
    
    if lat is not None and lon is not None:
        print("\n" + "="*60)
        print("RESULT FOUND:")
        print(f"Place queried : {place}")
        print(f"Matched address: {address}")
        print(f"Latitude      : {lat}")
        print(f"Longitude     : {lon}")
        print("="*60 + "\n")
    else:
        print("\n→ Could not find coordinates for this place.")
        print("  Try adding more details (city + state + country)")
        print("  Example: 'Palanpur, Banaskantha, Gujarat, India'\n")
    
    again = input("Want to search another place? (y/n): ").strip().lower()
    if again != 'y':
        print("\nThank you! Goodbye.\n")
        break
    
    time.sleep(0.5)  # small pause for better UX