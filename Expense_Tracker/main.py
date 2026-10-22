import tracker

### Menu Items ###
menu_options = (
    "Create New Expense Report",
    "Modify Expense Report",
    "List Expense Reports",
    "Quit"
)

### Prints User Options ###
def main():
    print("\nExpense Tracker Options:")
    while True:
        print()
        for number, option in enumerate(menu_options, start=1):
            print(f"{number}. {option}")
        choice = input("\nChoose an option: ")
        if choice == "1":
            break
        elif choice == "4":
            print("\nHave a good day!")
            break
        else:
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    main()