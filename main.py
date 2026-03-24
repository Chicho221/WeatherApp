from weather import get_weather, city_name_check, save_history, show_history, clear_history

def main():
    while True:
        print("\n1.Show Weather")
        print("2.Show History")
        print("3.Clear History")
        print("4.Exit")
        choice = input("Enter option: ")
        #Show Weather Option
        if choice == "1":
            while True:
                city = input("\nEnter city name (or 'exit'): ").lower()
                if city == "exit":
                    break
                if not city_name_check(city): # Check if name is valid (not a number)
                    print("Invalid city name.")
                    continue
                weather = get_weather(city)
                save_history(weather)
                if weather:
                    print(f"\n---- Weather Report ----")
                    print(f"City: {weather['city']}")
                    print(f"Temperature: {round(weather['temperature'], 1)}°C")
                    print(f"Weather: {weather['description'].title()}")
                break
        #Show History Option
        elif choice == "2":
            print("---- Weather History ----")
            history = show_history()
            for log in history:
                print(f"\nTime: {log["time"]} ")
                print(f"City: {log["city"]} ")
                print(f"Temperature: {log["temperature"]} ")
                print(f"Weather: {log["description"]} ")
        #Clear History Option
        elif choice == "3":
            while True:
                warning_choice = input("Are you sure? (y/n)")
                if warning_choice == "y":
                    clear_history()
                    break
                elif warning_choice == "n":
                    break
                else:
                    continue
        #Exit Option
        elif choice == "4":
            return

if __name__ == "__main__":
    main()