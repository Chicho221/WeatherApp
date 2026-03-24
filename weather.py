import requests
import json
from datetime import datetime
from api import API_KEY, BASE_URL

def city_name_check(city):
    return any(char.isalpha() for char in city)

def timestamp():
    time = datetime.now()
    formatted_time = time.strftime("%Y-%m-%d %H:%M")
    return formatted_time

def clear_history():
    with open("WeatherApp/history.json", "w") as file:
            pass
    
def show_history():
    try:
        with open("WeatherApp/history.json", "r") as file:
            history = json.load(file)
    except:
        history = []
    return history

def save_history(weather):
    history = show_history()
    
    history.append(weather)

    with open("WeatherApp/history.json", "w") as file:
        json.dump(history, file, indent=4)
        
def get_weather(city):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=parameters) 
        print("Request get | Success")
        if response.status_code == 404:
            print("City not found.")
            return None
        response.raise_for_status() #Check for errors
        print("Status check | Success")
        data = response.json()

        return {
            "time": timestamp(),
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.RequestException:
        print("Fetching failed")
        return None