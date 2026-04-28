import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_payment_status(status):
    allowed_statuses = {"Paid", "Partial", "Unpaid"}
    return status in allowed_statuses


def validate_positive_number(value):
    try:
        number = float(value)
        return number >= 0
    except ValueError:
        return False