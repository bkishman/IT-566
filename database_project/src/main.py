###Entry point for Database Project###

from expense_tracker import expense_tracker

# Goals for Project 3:
# 1) Less code in main.py
# 2) More mainstreamed, simplified code (no janky logic to make calls work)
# 3) Better directory structure

def main():
    expense_tracker.run()

if __name__ == "__main__":
    main()