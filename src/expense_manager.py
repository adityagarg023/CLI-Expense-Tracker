from models.expense import Expense
from src.file_manager import FileManager

class ExpenseManager:
    def __init__(self):
        self.file_manager = FileManager()
        self.expenses = []
        self.load()

    def load(self):
        expenses_list = self.file_manager.load_expenses()
        self.expenses = [Expense(**e) for e in expenses_list]

    def save(self):
        dict_list = [e.to_dict() for e in self.expenses]
        self.file_manager.save_expenses(dict_list)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.save()

    def delete_expense(self, serial_no):
        original_len = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.serial_no != serial_no]
        if len(self.expenses) == original_len:
            return False   # nothing deleted
        self.save()
        return True

    def update_expense(self, serial_no, date=None, amount=None, category=None, remark=None):
        for e in self.expenses:
            if e.serial_no == serial_no:
                if date: e.date = date
                if amount: e.amount = amount
                if category: e.category = category
                if remark: e.remark = remark
                self.save()
                return True
        return False

    def get_expenses(self):
        return self.expenses

    def search_expenses(self, serial_no):
        for e in self.expenses:
            if e.serial_no == serial_no:
                return e
        return None

    def get_by_serial(self, serial_no):
        for e in self.expenses:
            if e.serial_no == serial_no:
                return e
        return None
