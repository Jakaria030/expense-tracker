from tracker import Expense
from tracker import ExpenseStorage
from tracker import generate_id, get_datetime

def addExpense(date, category, amount, currency, note):
    expense = Expense(generate_id(), date, category, amount, currency, note, get_datetime())
    storage = ExpenseStorage()
    storage.add_expense(expense)