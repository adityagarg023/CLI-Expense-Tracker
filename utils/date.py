from datetime import datetime, date as dt_date

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return None

def format_date(date_obj):
    if not date_obj:
        return None
    return date_obj.strftime("%d-%m-%Y")

def is_future(date_obj):
    return date_obj > dt_date.today()

def month_year(date_obj):
    return date_obj.strftime("%m-%Y")

def is_valid_date(date_str):
    return parse_date(date_str) is not None
