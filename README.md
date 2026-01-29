# Expense Tracker CLI

A **Command-Line Interface (CLI) tool** to manage and track your personal expenses. Add, edit, delete, and list expenses, as well as generate summaries, directly from your terminal.

---

## Features

- Add, edit, and delete expenses
- Categorize expenses (e.g., Food, Transport, Entertainment)
- Filter and sort expenses by date, category, or amount
- Generate monthly or custom date-range summaries
- Export reports in table or CSV format
- Lightweight and easy to use

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jakaria030/expense-tracker.git
    cd expense-tracker
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # for linux
    Windows: venv\Scripts\activate # for windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

0. Run the CLI tool:
    
    ```bash
    python -m tracker <command> [options]
    ```
    The tool supports multiple commands:

1. Add a new expense
    ```bash
    python -m tracker add --category CATEGORY --amount AMOUNT [options]
    ```
    ### Options:
    | Option       | Description                               | Default |
    | ------------ | ----------------------------------------- | ------- |
    | `--date`     | Expense date in YYYY-MM-DD format         | Today   |
    | `--category` | Expense category (required)               | -       |
    | `--amount`   | Amount spent (required, must be positive) | -       |
    | `--currency` | Currency                                  | BDT     |
    | `--note`     | Optional note                             | ""      |

    #### Example:
    ```bash
    python -m tracker add --category Food --amount 250 --note "Lunch at cafe"
    ```

2. Delete an expense
    ```bash
    python -m tracker delete --id EXPENSE_ID
    ```
    #### Example:
    ```bash
    python -m tracker delete --id EXP-20260128-1234
    ```

3. Edit an expense
    ```bash
    python -m tracker edit --id EXPENSE_ID [options]
    ```
    ### Options:
    | Option       | Description                               
    | ------------ | ------------------      
    | `--category` | Update category
    | `--amount`   | Update amount
    | `--currency` | Update currency
    | `--note`     | Update note

    #### Example:
    ```bash
    python -m tracker edit --id EXP-20260128-1234 --amount 300 --note "Updated lunch"
    ```

4. Expense list
    ```bash
    python -m tracker list [options]
    ```
    ### Options:
    | Option       | Description                                  |
    | ------------ | -------------------------------------------- |
    | `--month`    | Filter by month (YYYY-MM)                    |
    | `--from`     | Filter from date (YYYY-MM-DD)                |
    | `--to`       | Filter to date (YYYY-MM-DD)                  |
    | `--category` | Filter by category                           |
    | `--min`      | Minimum amount                               |
    | `--max`      | Maximum amount                               |
    | `--sort`     | Sort by field (`amount`, `date`, `category`) |
    | `--desc`     | Sort descending(only pass flag)              |
    | `--limit`    | Limit number of results                      |
    | `--format`   | Output format (`table` or `csv`)             |

    #### Example:
    ```bash
    python -m tracker list --month 2026-01 --category Food --sort amount --desc
    ```

5. Expense summary
    ```bash
    python -m tracker summary [options]
    ```
    ### Options:
    | Option       | Description                    |
    | ------------ | ------------------------------ |
    | `--month`    | Summary by month (YYYY-MM)     |
    | `--from`     | Summary from date (YYYY-MM-DD) |
    | `--to`       | Summary to date (YYYY-MM-DD)   |
    | `--category` | Summary by category            |
    
    #### Example:
    ```bash
    python -m tracker summary --month 2026-01 --category Transport
    ```
## Project Structure
```bash
expense-tracker-cli/
│
├── tracker/                 # Main package
│   ├── __init__.py
│   ├── __main__.py          # Entry point for CLI: python -m tracker
│   ├── cli.py               # CLI parser and commands
│   ├── logger.py            # Logging setup
│   ├── service.py           # Business logic / expense management
│   ├── model.py             # Data models (Expense, etc.)
│   ├── utils.py             # Utility functions (date validation, amount check)
│   └── storage.py           # File storage logic
│
├── .gitignore               # Files/folders to ignore in git
├── requirements.txt         # Python dependencies
└── README.md                # Project README

```
