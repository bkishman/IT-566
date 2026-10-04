import diary

# Defining the main function of the program, entries, and files
def main():
    diary_file = "diary.txt"
    print("Welcome to your Diary!")
    date = input("Date (DD/MMM/YYYY): ")
    text = input("Entry: ")
    diary.add_entry(diary_file, date, text)
    entries = diary.read_entries(diary_file)
    for entry in entries:
        clean_entry = entry.strip()
        print(clean_entry)
    



if __name__ == "__main__":
    main()