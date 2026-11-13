###Creates, filters, exports expense reports###

import json
import csv
import glob
import os
from user_interface import user_interface

#Creates expense reports as a class
class ExpenseReport:
    def __init__(self, number, date):
        self.number = number
        self.date = date
        self.expenses = []

#Add expense function for new expense reports
    def add_expense (self, date, expense_category, amount, description):
        self.expenses.append({
            "date": date,
            "expense_category": expense_category,
            "amount": amount,
            "description": description
        })

#Save file as JSON function
    def save_file(self):
        with open(f"expense_report_{self.number}.json", "w") as file:
            json.dump(vars(self), file, indent=4)

#Function for exporting JSON files to CSV
    def export_csv(self):
        with open(f"expense_report_{self.number}.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "expense_category", "amount", "description"])
            writer.writeheader()
            writer.writerows(self.expenses)

#Function for filtering expense reports
    def filter_expenses(self, start_date="", end_date="", category=""):
        matches = []
        for expense in self.expenses:
            if start_date and expense["date"] < start_date:
                continue
            if end_date and expense["date"] > end_date:
                continue
            if category and expense["expense_category"] != category:
                continue
            matches.append(expense)
        return matches

#Function for loading files into memory for filtering
def load_file(filename):
    with open(filename) as file:
        data = json.load(file)
    report = ExpenseReport(data["number"], data["date"])
    report.expenses = data["expenses"]
    return report

def load_all_reports():
    reports = []
    for filename in glob.glob("expense_report_*.json"):
        reports.append(load_file(filename))
    return reports

#Primary run function. Calls user_interface menu options.
def run():
    user_interface.show_message("\nHooyah, Shipmate! Thanks for using the N1 Department Expense Tracker. Here are your options:")
    reports = load_all_reports()

    while True:
        choice = user_interface.show_menu()

        if choice == "1":
            number, date = user_interface.get_report_info()
            report = ExpenseReport(number, date)
            while True:
                report.add_expense(*user_interface.get_expense())
                if not user_interface.ask_add_another():
                    break
            report.save_file()
            reports.append(report)
            user_interface.show_message("\nReport saved.")

        elif choice == "2":
            start, end, category = user_interface.get_filter_info()
            found = False
            for report in reports:
                for expense in report.filter_expenses(start, end, category):
                    user_interface.show_expense(report.number, expense)
                    found = True
            if not found:
                user_interface.show_message("\nNo matching expenses.")

        elif choice == "3":
            number = user_interface.get_report_number("export")
            for report in reports:
                if report.number == number:
                    report.export_csv()
                    user_interface.show_message(f"\nExported to expense_report_{number}.csv")
                    break
            else:
                user_interface.show_message("\nReport not found.")

        elif choice == "4":
            number = user_interface.get_report_number("open")
            filename = f"expense_report_{number}.json"
            if os.path.exists(filename):
                os.startfile(filename)
            else:
                user_interface.show_message("\nReport not found.")

        elif choice == "5":
            print("\nHave a fine Navy day!")
            break

        else:
            user_interface.show_message("\nInvalid choice. Please choose another option.")