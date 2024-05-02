def save_birthdays_to_file(birthdays, file_path):
    with open(file_path, 'w') as file:
        for name, date in birthdays.items():
            file.write(f"{name},{date}\n")


def load_birthdays_from_file(file_path):
    birthdays = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, date = line.strip().split(',')
            birthdays[name] = date
    return birthdays


def display_reminders(birthdays):
    if not birthdays:
        print("No birthdays to display.")
    else:
        print("Birthday Reminders:")
        for name, date in birthdays.items():
            print(f"{name}: {date}")


def add_birthday(birthdays, name, date):
    birthdays[name] = date
    print(f"Added {name}'s birthday on {date}.")
    save_birthdays_to_file(birthdays, 'birthdays.txt')


def remove_birthday(birthdays, name):
    if name in birthdays:
        del birthdays[name]
        print(f"Removed {name}'s birthday.")
        save_birthdays_to_file(birthdays, 'birthdays.txt')
    else:
        print(f"{name} not found in birthdays.")


def main():
    birthdays = load_birthdays_from_file('birthdays.txt')

    while True:
        print("\n1. Display Birthday Reminders")
        print("2. Add a Birthday")
        print("3. Remove a Birthday")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_reminders(birthdays)
        elif choice == '2':
            name = input("Enter the name: ")
            date = input("Enter the date (MM/DD): ")
            add_birthday(birthdays, name, date)
        elif choice == '3':
            name = input("Enter the name to remove: ")
            remove_birthday(birthdays, name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
