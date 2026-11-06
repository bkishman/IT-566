import json
import csv

### Expense Tracker Primary Functions ###

#Class definition for Expense Report
class ExpenseReport:
    def __init__(self, number, date):
        self.number = number
        self.date = date
        self.expenses = []

    #Function for creating an expense to work in
    def add_expense(self, date, expense_category, amount, description=""):
        expense = {
            "date": date,
            "expense_category": expense_category,
            "amount": float(amount),
            "description": description,
        }
        self.expenses.append(expense)

    #Function to create JSON file
    def save_file(self):
        data = {
            "number": self.number,
            "date": self.date,
            "expenses": self.expenses,
        }
        filename = f"expense_report_{self.number}.json"
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        return filename

    #Function for exporting to CSV
    def export_csv(self):
        filename = f"expense_report_{self.number}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "expense_category", "amount", "description"])
            for expense in self.expenses:
                writer.writerow([
                    expense["date"],
                    expense["expense_category"],
                    expense["amount"],
                    expense["description"],
                ])
        return filename

    #Function for filtering expenses by date range and/or category
    def filter_expenses(self, start_date="", end_date="", category=""):
        results = []
        for expense in self.expenses:
            if start_date and expense["date"] < start_date:
                continue
            if end_date and expense["date"] > end_date:
                continue
            if category and expense["expense_category"].lower() != category.lower():
                continue
            results.append(expense)
        return results


#Function to open a saved JSON file as an ExpenseReport (not part of the class)
def load_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    report = ExpenseReport(data["number"], data["date"])
    report.expenses = data["expenses"]
    return report

#Function for selecting/modifying reports
#def modify_file():

#Function for listing available reports -- list all, or by date range
#def list_files():