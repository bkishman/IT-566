### Menu Items ###
menu_options = (
    "List Available Expense Reports",
    "Make New Expense Report",
    "Choose Expense Report to Modify",
    "View Expense Report",
    "Quit"
)
### Prints User Options ###
def expense_tracker():
    print("Expense Tracker Options:")
    while True:
        print()
        for number, option in enumerate(menu_options, start=1):
            print(f"{number}. {option}")
        choice = input("\nChoose an option: ")
        if choice == "1":
            break
        elif choice == "5":
            print("\nHave a good day!")
            break
        else:
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    expense_tracker()