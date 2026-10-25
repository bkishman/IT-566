import json
import csv

### Expense Tracker Primary Functions ###


#Class definition for Expense Report
class ExpenseReport:
    def __init__(self, number, date):
        self.number = number
        self.date = date
        self.expenses = []

#Function for creating an expense JSON to work in
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

#Function for selecting/modifying reports
#def modify_file():

#Function for listing available reports -- list all, or by date range
#def list_files():