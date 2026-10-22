### Expense Tracker Primary Functions ###

#Class definition for Expense Report
class Expense_Report:
    def __init__(self, number, date):
        self.number = number
        self.date = date

#Function for creating an expense JSON to work in
def create_file():