from weather import get_weather, city_name_check

def main():
    while True:
        city = input("Enter city: ").lower()
        if not city_name_check(city): # Check if name is valid (not a number)
            print("Invalid city name.")
            continue
        break

    weather = get_weather(city)

    if weather:
        print(f"\n---- Weather Report ----")
        print(f"City: {weather['city']}")
        print(f"Temperature: {round(weather['temperature'], 1)}°C")
        print(f"Weather: {weather['description'].title()}")

if __name__ == "__main__":
    main()