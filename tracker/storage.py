import os
import json
from tracker import Expense
import csv
import sys
from tabulate import tabulate
from tracker.utils import filter_by_month, filter_by_date_from, filter_by_date_to, filter_by_category

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

    # delete an expense
    def delete_expense(self, id):
        data = self.expenses

        index = -1
        for indx in range(len(data)):
            if data[indx].id == id:
                index = indx
                break

        if index == -1:
            print("Id not found!")
            return
        
        data.pop(index)
        self.save_expenses()
        print(f"Delete: {id} data is deleted!")

    # edit an expense data
    def edit_expense(self, id, category, amount, currency, note):
        data = self.expenses
        
        ok = True
        for d in data:
            if d.id == id:
                ok = False
                d.category = category if category is not None else d.category
                d.amount = amount if amount is not None else d.amount
                d.currency = currency if currency is not None else d.currency
                d.note = note if note is not None else d.note
                break

        if ok:
            print("Id not found!")
            return
        
        self.save_expenses()
        print(f"Edit: {id} data is updated!")

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
            data = filter_by_month(data, month)
        if date_from:
            data = filter_by_date_from(data, date_from)
        if date_to:
            data = filter_by_date_to(data, date_to)
        if category:
            data = filter_by_category(data, category)
        if min:
            data = [r for r in data if r.amount >= min]
        if max:
            data = [r for r in data if r.amount <= max]

        # --- Sorting ---
        if sort:
            data.sort(key=lambda r: getattr(r, sort, None), reverse=desc)

        # --- Limit ---
        if limit:
            data = data[:limit]

        if not data:
            print("No records found!")
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
            print(tabulate(rows, headers="keys"))
    
    # summary expenses data
    def summary_expenses(self, month, date_from, date_to, category):
        # print(month, date_from, date_to, category)

        data = self.expenses

        # --- Filtering ---
        if month:
            data = filter_by_month(data, month)
        if date_from:
            data = filter_by_date_from(data, date_from)
        if date_to:
            data = filter_by_date_to(data, date_to)
        if category:
            data = filter_by_category(data, category)

        # --- Format data to display ---
        if not data:
            print("No records found!")
            return

        title = "Summary:"
        if month:
            title += f" (Month - {month})"
        if date_from:
            title += f" (From - {date_from})"
        if date_to:
            title += f" (To - {date_to})"
        if category:
            title += f" (Category - {category})"

        print(title)
        print(f"Total Expenses: {len(data)}")

        # --- Summary: grand total by curreny ---
        grand_totals = {}
        for d in data:
            grand_totals[d.currency] = grand_totals.get(d.currency, 0) + d.amount


        for key, value in grand_totals.items():
            print(f"Grand Total: {value} {key}")

        # --- By category: filter by category and currency
        print("\nBy Category:")
        categories = {}
        for d in data:
            key = f"{d.category}-{d.currency}"
            categories[key] = categories.get(key, 0) + d.amount

        for key, value in categories.items():
            category = key.split("-")[0]
            currency = key.split("-")[1]
            print(f"{category.capitalize()} {value} {currency}")
