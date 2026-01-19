from datetime import date, datetime

ALLOWED_CATEGORIES = {
    "food",
    "transport",
    "rent",
    "utilities",
    "entertainment",
    "shopping",
    "other"
}

def validate_serial_no(serial_no, existing_expenses):
    if not isinstance(serial_no, int):
        return False, "Serial number must be an integer"
    if serial_no < 1:
        return False, "Serial number must be positive"
    for e in existing_expenses:
        if e.serial_no == serial_no:
            return False, "Serial number already exists"
    return True, None

def validate_date(date_value, required=True):
    if not date_value:
        if required:
            return False, "Date can't be empty"
        else:
            return True, None

    if isinstance(date_value, date):
        date_str = date_value.strftime("%d-%m-%Y")
    else:
        date_str = str(date_value)

    try:
        parsed_date = datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return False, "Date must be in DD-MM-YYYY format"

    if parsed_date > date.today():
        return False, "Date can't be in the future"

    return True, None

def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        return False, "Amount must be a number"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    return True, None
    
def validate_category(category):
    if not category:
        return False, "Category can't be empty"
    if category.lower() not in ALLOWED_CATEGORIES:
        return False, f"Category must be one of {ALLOWED_CATEGORIES}"
    return True, None

def validate_remark(remark):
    if remark is None:
        return True, None
    if not isinstance(remark, str):
        return False, "Remark must be a string"
    if len(remark) > 100:
        return False, "Remark can't exceed 100 characters"
    return True, None

def validate_expense(expense, existing_expenses, is_update=False):
    if not is_update:
        ok, err = validate_serial_no(expense.serial_no, existing_expenses)
        if not ok:
            return False, err

    ok, err = validate_date(expense.date, required=not is_update)
    if not ok:
        return False, err

    ok, err = validate_amount(expense.amount)
    if not ok:
        return False, err

    ok, err = validate_category(expense.category)
    if not ok:
        return False, err

    ok, err = validate_remark(expense.remark)
    if not ok:
        return False, err

    return True, None