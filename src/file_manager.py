import csv, os

CSV_FILE = "data/expense.csv"

class FileManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["serial_no", "date", "amount", "category", "remark"])

    def load_expenses(self):
        expense = []
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                row['serial_no'] = int(row['serial_no'])
                expense.append(row)
        return expense

    def save_expenses(self, expense):
        if not expense:
            return
        headers = expense[0].keys()
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(expense)