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