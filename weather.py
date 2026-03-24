import requests
import json
from datetime import datetime
from api import API_KEY, BASE_URL

class WeatherManager:
    #Check if input is alphabetic
    def city_name_check(self, city):
        return any(char.isalpha() for char in city)
    #Makes timestamp
    def timestamp(self):
        time = datetime.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M")
        return formatted_time
    #Clears history.json
    def clear_history(self):
        with open("WeatherApp/history.json", "w") as file:
                pass
    #Displays history    
    def show_history(self):
        try:
            with open("WeatherApp/history.json", "r") as file:
                history = json.load(file)
        except:
            history = []
        return history
    #Saves history
    def save_history(self,weather):
        if weather == None:
            return
        history = self.show_history()
        history.append(weather)

        with open("WeatherApp/history.json", "w") as file:
            json.dump(history, file, indent=4)
    #Fetches weather information        
    def get_weather(self, city):
        parameters = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(BASE_URL, params=parameters) 
            if response.status_code == 404:
                print("City not found.")
                return None
            response.raise_for_status() #Check for errors
            data = response.json()

            return {
                "time": self.timestamp(),
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        except requests.RequestException:
            print("Fetching failed")
            return None