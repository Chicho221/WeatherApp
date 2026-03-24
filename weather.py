import requests
import json
from api import API_KEY, BASE_URL

def get_weather(city):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=parameters) 
        print("Request get | Success")
        response.raise_for_status() #Check for errors
        print("Status check | Success")
        data = response.json()

        #Dumps weather parameters in json file (for personal use and future upgrades)
        with open ("WeatherApp/weather.json", "w") as file:
            json.dump(data, file, indent=4)

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.RequestException:
        print("Fetching failed")
        return None