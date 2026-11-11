#GUI Interface Options

### Menu Items ###
menu_options = (
    "Add Expense Report",
    "Filter Expense Reports",
    "Export Report to CSV",
    "Open Expense Report",
    "Quit"
)

def show_menu():
    print()
    for number, option in enumerate(menu_options, start=1):
        print(f"{number}. {option}")
    return input("\nChoose an option: ")