from datetime import datetime
import argparse
from tracker.logger import get_logger

# logger
logger = get_logger()

# valid date YYYY-MM-DD
def valid_date(value):
    try:
        dt = datetime.strptime(value, "%Y-%m-%d").date()
        return dt.isoformat()
    except ValueError:
        logger.error("Message: Date must be YYYY-MM-DD")
        raise argparse.ArgumentTypeError("Date must be YYYY-MM-DD")

# positive number
def positive_amount(value):
    try:
        value = float(value)
    except ValueError:
        logger.error("Message: Amount must be a number")
        raise argparse.ArgumentTypeError("Amount must be a number")

    if value <= 0:
        logger.error("Message: Amount must be > 0")
        raise argparse.ArgumentTypeError("Amount must be > 0")

    return value

# today's date
def get_date():
   return datetime.now().strftime("%Y-%m-%d")

# generate id
def generate_id():
    dt = datetime.now()
    return f"EXP-{dt.year}{dt.month:02d}{dt.day:02d}-{dt.microsecond // 100 :04d}"

# generate iso date time
def get_datetime():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# filter by month YYYY-MM
def filter_by_month(data, month):
    return [d for d in data if d.date.startswith(month)]

# filter by date from
def filter_by_date_from(data, date_from):
    return [d for d in data if d.date >= date_from]

# filter by date to
def filter_by_date_to(data, date_to):
    return [d for d in data if d.date <= date_to]

# filter by category
def filter_by_category(data, category):
    return [d for d in data if d.category.lower() == category.lower()]


# command generator
def command_generator(
    base_command,
    date=None,
    category=None,
    amount=None,
    currency=None,
    note=None,
    id=None,
    month=None,
    date_from=None,
    date_to=None,
    min=None,
    max=None,
    sort=None,
    desc=None,
    limit=None,
    format=None
):
    message = f"Command: {base_command}"

    # Add optional arguments if they are exist
    if date:
        message += f" --date {date}"
    if category:
        message += f" --category {category}"
    if amount:
        message += f" --amount {amount}"
    if currency:
        message += f" --currency {currency}"
    if note:
        message += f" --note {note}"
    if id:
        message += f" --id {id}"
    if month:
        message += f" --month {month}"
    if date_from:
        message += f" --from {date_from}"
    if date_to:
        message += f" --to {date_to}"
    if min:
        message += f" --min {min}"
    if max:
        message += f" --max {max}"
    if sort:
        message += f" --sort {sort}"
    if desc:
        message += f" --desc"
    if limit:
        message += f" --limit {limit}"
    if format:
        message += f" --format {format}"

    return message
