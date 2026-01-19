from collections import defaultdict

def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e.amount
    return total

def category_summary(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return dict(summary)

def monthly_summary(expenses):    
    summary = defaultdict(float)
    for e in expenses:
        _, month, year = e.date.split("-")
        key = f"{month}-{year}"
        summary[key] += e.amount
    return dict(summary)    

def highest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda e: e.amount)

def lowest_expense(expenses):
    if not expenses:
        return None
    return min(expenses, key=lambda e: e.amount)