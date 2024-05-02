def load_birthdays_from_file(file_path):
    birthdays = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, date = line.strip().split(',')
                birthdays[name] = date
    except FileNotFoundError:
        print("File not found. Creating a new file.")
    return birthdays


def save_birthdays_to_file(birthdays, file_path):
    with open(file_path, 'w') as file:
        for name, date in birthdays.items():
            file.write(f"{name},{date}\n")
    print("Birthdays saved to file.")


def display_reminders(birthdays):
    if birthdays:
        print("Birthday Reminders:")
        for name, date in birthdays.items():
            print(f"{name}: {date}")
    else:
        print("No birthday reminders.")


def add_birthday_manually(birthdays):
    name = input("Enter the name: ")
    date = input("Enter the date (MM/DD): ")
    birthdays[name] = date
    print(f"{name}'s birthday added on {date}.")


def add_birthday_from_file(birthdays):
    file_name = input("Enter the file name  (with .txt extension): ")
    if file_name.endswith('.txt'):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    name, date = line.strip().split(',')
                    birthdays[name] = date
            print("Birthdays added from file.")
        except FileNotFoundError:
            print("File not found. Please make sure the file exists.")
    else:
        print("Please enter a file with a .txt extension.")


def remove_birthday(birthdays):
    name = input("Enter the name to remove: ")
    if name in birthdays:
        del birthdays[name]
        print(f"{name}'s birthday removed.")
    else:
        print("Birthday not found.")


def main():
    file_path = input("file name to store birthdays (with .txt extension): ")
    birthdays = load_birthdays_from_file(file_path)
    while True:
        print("\nBirthday Reminder")
        print("1. Display Birthday Reminders")
        print("2. Add a Birthday")
        print("3. Remove a Birthday")
        print("4. Save Birthdays to File")
        print("5. Load Birthdays from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_reminders(birthdays)
        elif choice == '2':
            add_choice = input("Add birthdays manually(m) or from a file(f)? ")
            if add_choice.lower() == 'm':
                add_birthday_manually(birthdays)
            elif add_choice.lower() == 'f':
                add_birthday_from_file(birthdays)
            else:
                print("Please enter'm' for manual or'f' for file.")
        elif choice == '3':
            remove_birthday(birthdays)
        elif choice == '4':
            save_choice = input("file name to save birthdays(.txt extension):")
            save_birthdays_to_file(birthdays, save_choice)
        elif choice == '5':
            load_choice = input("file name to load birthdays from(.txt extension):")
            birthdays = load_birthdays_from_file(load_choice)
            print("Birthdays loaded from file.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
