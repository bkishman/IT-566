import diary

def main():
    print("Welcome to your Diary!")
    diary.add_entry("01/JAN/2026", "  Lunch  ")
    entries = diary.read_entries()
    for entry in entries:
        print(entry)
    



if __name__ == "__main__":
    main()