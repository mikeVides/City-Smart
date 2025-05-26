import requests
import json
import os
from city_list import cities
from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv('WEATHER_API_KEY')

def get_coords(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city},{state},US",
        "limit": 1,
        "appid": WEATHER_API
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data:
        return {
            "city": city,
            "state": state,
            "lat": data[0]['lat'],
            "lon": data[0]['lon']
        }
    else:
        print(f"Coordinates not found for {city}, {state}")
        return None

def main():
    coords_list = []

    for city_obj in cities:
        coords = get_coords(city_obj["city"], city_obj["state"])
        if coords:
            coords_list.append(coords)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    output_path = os.path.join(script_dir, "city_coordinates.json")

    with open(output_path, "w") as f:
        json.dump(coords_list, f, indent=2)

    print(f"Saved coordinates to {output_path}")

if __name__ == "__main__":
    main()