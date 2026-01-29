from datetime import datetime
import argparse

# valid date YYYY-MM-DD
def valid_date(value):
    try:
        dt = datetime.strptime(value, "%Y-%m-%d").date()
        return dt.isoformat()
    except ValueError:
        raise argparse.ArgumentTypeError("date must be YYYY-MM-DD")

# positive number
def positive_amount(value):
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("amount must be a number")

    if value <= 0:
        raise argparse.ArgumentTypeError("amount must be > 0")

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