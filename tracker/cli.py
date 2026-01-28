from argparse import ArgumentParser
from tracker import valid_date, positive_amount, get_date
from tracker import addExpense


# program start from main function
def main():
    parser = ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- add command ----
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--date", type=valid_date, default=get_date(), help="Expense date (YYYY-MM-DD), default: today")
    add_parser.add_argument("--category", required=True, help="Expense category")
    add_parser.add_argument("--amount", required=True, type=positive_amount, help="Amount spent")
    add_parser.add_argument("--currency", default="BDT", help="Currency")
    add_parser.add_argument("--note", default="", help="Optional note")
    




    args = parser.parse_args()
    
    # match the which command run
    match args.command:
        case "add":
            addExpense(args.date, args.category, args.amount, args.currency, args.note)



    