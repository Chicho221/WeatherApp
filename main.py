from weather import get_weather

def main():
    city = input("Enter city: ")

    weather = get_weather(city)

    if weather:
        print(f"\nCity: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")

if __name__ == "__main__":
    main()