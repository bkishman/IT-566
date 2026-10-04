import diary

# Defining the main function of the program, entries, and files
def main():
    diary_file = "diary.txt"
    print("Welcome to your Diary!")
    while True:
        print("\n1. Add an entry")
        print("2. Print all entries")
        print("3. Quit")
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
        elif choice == "3":
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