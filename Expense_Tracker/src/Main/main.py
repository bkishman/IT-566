import tracker

### Menu Items ###
menu_options = (
    "Add Expense Report",
    "Modify Expense Report",
    "List Expense Reports",
    "Export Report to CSV",
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
            if not reports:
                ###TYPE ERROR?###
                print("\nNo reports to export. Add a report first.")
            else:
                export_number = input("\nEnter report number to export: ")
                found = False
                for report in reports:
                    if report.number == report.export:
                        filename = report.export_csv()
                        print(f"\nReport {report.number} exported to {filename}")
                        found = True
                        break
                if not found:
                    ###TYPE ERROR?###
                    print("\nReport not found.")
        elif choice == "6":
            print("\nHave a fine Navy day!")
            break
        else:
            ###TYPE ERROR?###
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    main()