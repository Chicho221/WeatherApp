from weather import get_weather, city_name_check

def main():
    while True:
        city = input("Enter city: ")
        if not city_name_check(city): # Check if name is valid (not a number)
            print("Invalid city name.")
            continue
        break
    
    weather = get_weather(city)

    if weather:
        print(f"\nCity: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")

if __name__ == "__main__":
    main()