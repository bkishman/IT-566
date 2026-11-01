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


# Check to make sure diary entry actually exists before read
def file_exists(file_name):
    try:
        with open(file_name, "r"):
            return True
    except FileNotFoundError:
        return False


# Creating a new diary entry
def create_diary(file_name):
    with open (file_name, "a"):
        pass


# For filtering entries - uses same format as above for filename/date, 
def filter_entries(file_name, date):
    clean_date = date.strip().title()
    matches = []
    for line in read_entries(file_name):
        entry_date, text = line.strip().split(": ", 1)
        if entry_date == clean_date:
            matches.append(line.strip())
    return matches