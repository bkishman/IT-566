#User Interface Options

### Menu Items ###
menu_options = (
    "Add Expense Report",
    "Filter Expense Reports",
    "Export Report to CSV",
    "Open Expense Report",
    "Quit"
)

def show_menu():
    print()
    for number, option in enumerate(menu_options, start=1):
        print(f"{number}. {option}")
    return input("\nChoose an option: ")

def get_report_info():
    number = input("\nReport number: ")
    date = input("\nReport date (YYYY-MM-DD): ")
    return number, date

def get_expense():
    return (
        input("\nExpense date (YYYY-MM-DD): "),
        input("\nCategory: "),
        float(input("\nAmount: ")),
        input("\nDescription: "),
    )

def ask_add_another():
    return input("Add another expense? (y/n): ").lower() == "y"

def get_filter_info():
    start = input("\nStart date (blank for none): ")
    end = input("\nEnd date (blank for none): ")
    category = input("\nCategory (blank for none): ")
    return start, end, category

def get_report_number(action):
    return input(f"\nReport number to {action}: ")

def show_expense(report_number, expense):
    print(f"\nReport {report_number}: {expense['date']} | {expense['expense_category']} | ${expense['amount']:.2f} | {expense['description']}")

def show_message(text):
    print(text)