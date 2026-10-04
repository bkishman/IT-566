# Defining how an entry is formatted when called by main.py
def add_entry(file_name, date, text):
    clean_date = date.title()
    clean_text = text.strip()
    with open(file_name, "a") as file:
        file.write(f"{clean_date}: {clean_text}\n")


# Defining what read_entries does when called in main.py
def read_entries(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        return lines