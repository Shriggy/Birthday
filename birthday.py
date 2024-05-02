
birthdays = {}


def add_birthday(name, date):
    birthdays[name] = date
    print(f"Added {name}'s birthday on {date}.")
    print("Updated birthdays dictionary:", birthdays)


def remove_birthday(name):
    if name in birthdays:
        del birthdays[name]
        print(f"Removed {name}'s birthday.")
    else:
        print(f"{name}'s birthday not found.")


def display_reminders():
    if birthdays:
        reminders = []
        for name, date in birthdays.items():
            reminders.append(f"{name}: {date}")
        return reminders
    else:
        return []


def main():
    while True:
        print("\nMenu:")
        print("1. Add Birthday")
        print("2. Remove Birthday")
        print("3. Display Reminders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            date = input("Enter the date (MM/DD): ")
            add_birthday(name, date)
        elif choice == "2":
            name = input("Enter the name: ")
            remove_birthday(name)
        elif choice == "3":
            display_reminders()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
