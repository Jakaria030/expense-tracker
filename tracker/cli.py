from argparse import ArgumentParser
from tracker import valid_date, positive_amount, get_date
from tracker import addExpense, listExpenses


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
    
    # ---- list command ----
    list_parser = subparsers.add_parser("list", help="List expenses")
    list_parser.add_argument("--month", type=str, help="Filter by YYYY-MM")
    list_parser.add_argument("--from", dest="date_from", type=str, help="Filter from date YYYY-MM-DD")
    list_parser.add_argument("--to", dest="date_to", type=str, help="Filter to date YYYY-MM-DD")
    list_parser.add_argument("--category", type=str, help="Filter by category")
    list_parser.add_argument("--min", type=float, help="Minimum amount")
    list_parser.add_argument("--max", type=float, help="Maximum amount")
    list_parser.add_argument("--sort", type=str, default="date", help="Sort by field (amount, date, category)")
    list_parser.add_argument("--desc", action="store_true", help="Sort descending")
    list_parser.add_argument("--limit", type=int, help="Limit number of results")
    list_parser.add_argument("--format", type=str, default="table", help="Output format like table or csv")

    args = parser.parse_args()
    
    # match the which command run
    match args.command:
        case "add":
            addExpense(args.date, args.category, args.amount, args.currency, args.note)
        case "list":
            listExpenses(args.month, args.date_from, args.date_to, args.category, args.min, args.max, args.sort, args.desc, args.limit, args.format)



    