import os
import json
from tracker import Expense

# inital value save into data/expenses.json
initial_data = {"version": 1, "expenses": []}

class ExpenseStorage:
    filename = "data/expenses.json"

    def __init__(self):
        self.expenses = self.load_expenses() # all data load first and store expenses variable

         # ensure folder exists
        folder = os.path.dirname(self.filename)
        if folder:
            os.makedirs(folder, exist_ok=True)

        # ensure file exists
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write(json.dumps(initial_data, indent=4))

    # load data from data/expenses.json
    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                data = json.loads(file.read())
                return [Expense(**expense) for expense in data.get("expenses", [])]
        except:
            return []

    # save expenses data into data/expenses.json
    def save_expenses(self):
        try:
            with open(self.filename, "w") as file:
                expenses_list = [expense.to_dict() for expense in self.expenses]
                to_save = {"version": 1, "expenses": expenses_list}
                file.write(json.dumps(to_save, indent=4))
        except:
            print(f"Error: Something went wrong when writting!")

    # add expense data
    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    # get expenses data
    def get_expenses(self):
        return {"version": 1, "expenses": self.load_expenses()}
        