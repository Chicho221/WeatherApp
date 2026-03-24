from weather import get_weather, city_name_check

def main():
    while True:
        city = input("\nEnter city name (or 'exit'): ").lower()
        if city == "exit":
            break
        if not city_name_check(city): # Check if name is valid (not a number)
            print("Invalid city name.")
            continue
        weather = get_weather(city)

        if weather:
            print(f"\n---- Weather Report ----")
            print(f"City: {weather['city']}")
            print(f"Temperature: {round(weather['temperature'], 1)}°C")
            print(f"Weather: {weather['description'].title()}")
            continue
        break

if __name__ == "__main__":
    main()