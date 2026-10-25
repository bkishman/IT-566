import tracker

### Menu Items ###
menu_options = (
    "Add Expense Report",
    "Modify Expense Report",
    "List Expense Reports",
    "Quit"
)

### Prints User Options ###
def main():
    reports = []
    print("\nHooyah, Shipmate! Thanks for using the N1 Department Expense Tracker. Here are your options:")
    while True:
        print()
        for number, option in enumerate(menu_options, start=1):
            print(f"{number}. {option}")
        choice = input("\nChoose an option: ")
        if choice == "1":
            report_number = input("\nEnter report number: ")
            report_date = input("Enter report date (YYYY-MM-DD): ")
            report = tracker.ExpenseReport(report_number, report_date)

            while True:
                print("\nEnter an expense: ")
                expense_date = input("Date (YYYY-MM-DD): ")
                expense_category = input("Category: ")
                amount = input("Amount: ")
                description = input("Description (optional): ")
                report.add_expense(expense_date, expense_category, amount, description)

                another = input("\nAdd another expense? (y/n): ")
                if another.lower() != "y":
                    break
            reports.append(report)
            filename = report.save_file()
            print(f"\nReport {report.number} saved to {filename}")
        elif choice == "4":
            print("\nHave a fine Navy day!")
            break
        else:
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    main()