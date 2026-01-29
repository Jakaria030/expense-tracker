import os
import json
from tracker import Expense
import csv
import sys
from tabulate import tabulate

# inital value save into data/expenses.json
initial_data = {"version": 1, "expenses": []}

class ExpenseStorage:
    filename = "data/expenses.json"

    def __init__(self):
        # all data load first and store expenses variable
        self.expenses = self.load_expenses()

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
        except Exception as e:
            print(f"Error writing file: {e}")

    # add expense data
    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()
        self.display_add_message(expense)

    # get expenses data
    def get_expenses(self):
        return {"version": 1, "expenses": self.load_expenses()}
    
    # display message
    def display_add_message(self, expense):
        print(f"Added: {expense.id} | {expense.date} | {expense.category} | {expense.amount} | {expense.currency} | {expense.note} | {expense.created_at}")

    def list_expenses(self, month, date_from, date_to, category, min, max, sort, desc, limit, format):
        # print(month, date_from, date_to, category, min, max, sort, desc, limit, format)
        data = self.expenses

        # --- Filtering ---
        if month:
            data = [r for r in data if r.date.startswith(month)]
        if date_from:
            data = [r for r in data if r.date >= date_from]
        if date_to:
            data = [r for r in data if r.date <= date_to]
        if category:
            data = [r for r in data if r.category == category]
        if min is not None:
            data = [r for r in data if r.amount >= min]
        if max is not None:
            data = [r for r in data if r.amount <= max]

        # --- Sorting ---
        if sort:
            data.sort(key=lambda r: getattr(r, sort, None), reverse=desc)

        # --- Limit ---
        if limit:
            data = data[:limit]

        if not data:
            print("No records found.")
            return

        # --- Printing ---
        # Convert to dicts for formatting
        rows = []
        for r in data:
            rows.append({
                "ID": r.id,
                "Date": r.date,
                "Category": r.category,
                "Amount": r.amount,
                "Currency": r.currency,
                "Note": r.note
            })

        if format == "csv":
            writer = csv.DictWriter(sys.stdout, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        else:
            # Pretty table using tabulate
            print(tabulate(rows, headers="keys"))