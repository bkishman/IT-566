import sys
from pathlib import Path
import os
import glob

#added to pull tracker and gui from sibling folders
SRC = Path(__file__).resolve().parent.parent
sys.path.append(str(SRC / "tracker"))
sys.path.append(str(SRC / "gui_interface"))

import tracker
import gui_interface


### Runs Options from GUI ###
def main():
    reports = []
    for file_name in glob.glob("expense_report_*.json"):
        reports.append(tracker.load_file(file_name))

    print("\nHooyah, Shipmate! Thanks for using the N1 Department Expense Tracker. Here are your options:")

    while True:
        choice = gui_interface.show_menu()

        #Function for adding a new report
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

        #Function for filtering reports    
        elif choice == "2":
            if not reports:
                print("\nNo reports available. Add a report first.")
            else:
                print("\nLeave a filter blank to skip it.")
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

        #Function for exporting to CSV
        elif choice == "3":
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

        #Function for opening JSON file
        elif choice == "4":
            report_number = input("Enter report number to open: ")
            file_name = f"expense_report_{report_number}.json"
            if os.path.exists(file_name):
                os.startfile(file_name)
            else:
                print("File not found.")

        #Exit program        
        elif choice == "5":
            print("\nHave a fine Navy day!")
            break
        else:
            print("\nInvalid choice. Please choose another option.")






if __name__ == "__main__":
    main()