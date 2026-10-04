import diary

# Defining the main function of the program, entries, and files
def main():
    diary_file = "diary.txt"
    print("Welcome to your Diary!")
    while True:
        print("\n1. Add an entry")
        print("2. Print all entries")
        print("3. Filter entries by date")
        print("4. Choose diary file")
        print("5. Create a new diary file")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Date (DD/MMM/YYYY): ")
            text = input("Entry: ")
            diary.add_entry(diary_file, date, text)
            print("\nEntry saved.")
        elif choice == "2":
            if diary.file_exists(diary_file):
                entries = diary.read_entries(diary_file)
                for entry in entries:
                    clean_entry = entry.strip()
                    print(clean_entry)
            else:
                print("No diary file found yet. Add an entry first")
        elif choice == "4":
            new_file = input("Diary file name: ").strip()
            if new_file == "":
                print("No file name entered. Keeping the current diary.")
            elif diary.file_exists(new_file):
                diary_file = new_file
                print(f"Loaded {diary_file}.")
            else:
                print(f"\n{new_file} doesn't exist. Choose option 5 to create a new file.")
        elif choice == "5":
            new_file = input("New diary file name: ").strip()
            if new_file == "":
                print("No file name entered. Keeping the current diary.")
            elif diary.file_exists(new_file):
                print(f"\n{new_file} already exists. Use option 4 to load it.")
            else:
                diary.create_diary(new_file)
                diary_file = new_file
                print(f"Created and loaded {diary_file}.")
        elif choice == "6":
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

# Save for later
    # date = input("Date (DD/MMM/YYYY): ")
    # text = input("Entry: ")
    # diary.add_entry(diary_file, date, text)
    # entries = diary.read_entries(diary_file)
    # for entry in entries:
        # clean_entry = entry.strip()
        # print(clean_entry)
    



if __name__ == "__main__":
    main()