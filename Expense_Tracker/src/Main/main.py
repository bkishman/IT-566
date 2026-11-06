import sys
from pathlib import Path

#added to pull tracker and gui from sibling folders
SRC = Path(__file__).resolve().parent.parent
sys.path.append(str(SRC / "tracker"))
sys.path.append(str(SRC / "gui_interface"))

import tracker
import gui_interface


### Runs Options from GUI ###
def main():
    reports = []
    print("\nHooyah, Shipmate! Thanks for using the N1 Department Expense Tracker. Here are your options:")

    while True:
        choice = gui_interface.show_menu()


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

        elif choice == "2":
            print("\nNOT AVAILABLE")
            
        elif choice == "3":
            if not reports:
                print("\nLeave a filter blank to skip it.")
            else:
                start_date = input("Start date (YYYY-MM-DD): ")
                end_date = input("End date (YYYY-MM-DD): ")
                category = input("Category: ")

                match_count = 0
                for report in reports:
                    matches = report.filter_expenses(start_date, end_date, category)
                    for expense in matches:
                        print(f"Report {report.number} | {expense['date']} | {expense['expense_category']} | ${expense['amount']:.2f} | {expense['description']}")
                        match_count += 1

                if match_count == 0:
                    print("\nNo expenses matched.")

        elif choice == "4":
            if not reports:
                print("\nNo reports to export. Add a report first.")
            else:
                export_number = input("\nEnter report number to export: ")
                found = False
                for report in reports:
                    if report.number == export_number:
                        filename = report.export_csv()
                        print(f"\nReport {report.number} exported to {filename}")
                        found = True
                        break
                if not found:
                    print("\nReport not found.")

        elif choice == "5":
            filename = input("\nEnter the file name to open.")
            try:
                report = tracker.load_file(filename)
                reports.append(report)
                print(f"\nReport {report.number} loaded with {len(report.expenses)} expense(s).")
            except FileNotFoundError:
                print("\nFile not found.")
        elif choice == "6":
            print("\nHave a fine Navy day!")
            break
        else:
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    main()