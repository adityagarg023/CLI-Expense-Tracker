class Expense:
    def __init__(self, serial_no,  date, amount, category, remark):
        self.serial_no = serial_no
        self.date = date
        self.amount = amount
        self.category = category
        self.remark = remark

    def to_dict(self):
        return {
            "serial_no": self.serial_no,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "remark": self.remark
        }
