def add_entry(date, text):
    clean_date = date.title()
    clean_text = text.strip()
    with open("diary.txt", "a") as file:
        file.write(f"{clean_date}--{clean_text}\n")

def read_entries():
    with open("diary.txt", "r") as file:
        lines = file.readlines()
        return lines