from tracker import Expense
from tracker import ExpenseStorage
from tracker import generate_id, get_datetime

# add expense data
def addExpense(date, category, amount, currency, note):
    expense = Expense(generate_id(), date, category, amount, currency, note, get_datetime())
    storage = ExpenseStorage()
    storage.add_expense(expense)

# delete an expense
def deleteExpense(id):
    storage = ExpenseStorage()
    storage.delete_expense(id)

# list expense data
def listExpenses(month, date_from, date_to, category, min, max, sort, desc, limit, format):
    storage = ExpenseStorage()
    storage.list_expenses(month, date_from, date_to, category, min, max, sort, desc, limit, format)

# summary expenses data
def summaryExpenses(month, date_from, date_to, category):
    storage = ExpenseStorage()
    storage.summary_expenses(month, date_from, date_to, category)