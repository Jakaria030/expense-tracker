from tracker import Expense
from tracker import ExpenseStorage

# program start from main function
def main():
    es = ExpenseStorage()
    expens = Expense("EXP-1", "2026-01-28", "food", 250.50, "BDT", "Lunch", "2026-01-28T13:32:45")
    es.add_expense(expens)

    data = es.get_expenses()

    expenses = data.get("expenses", [])
    for e in expenses:
        print(e.__dict__)