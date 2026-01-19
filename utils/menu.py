from src.expense_manager import ExpenseManager
from models.expense import Expense
from src import summary
from utils.validator import validate_expense

def menu():
    manager = ExpenseManager()

    while True:
        print("\n==== Expense Tracker ====")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. View Summaries")
        print("6. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            expenses = manager.get_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for e in expenses:
                    print(f"{e.serial_no} | {e.date} | {e.amount} | {e.category} | {e.remark}")

        elif choice == "2":
            try:
                serial_no = int(input("Serial No: "))
                date_str = input("Date (DD-MM-YYYY): ").strip()
                amount = float(input("Amount: "))
                category = input("Category: ").strip().capitalize()
                remark = input("Remark (optional): ").strip() or None
                new_expense = Expense(
                    serial_no=serial_no,
                    date=date_str,
                    amount=amount,
                    category=category,
                    remark=remark
                )
                ok, err = validate_expense(new_expense, manager.get_expenses(), is_update=False)
                if not ok:
                    print("Error:", err)
                else:
                    manager.add_expense(new_expense)
                    print("Expense added successfully.")
            except ValueError:
                print("Invalid input type.")

        elif choice == "3":
            try:
                serial_no = int(input("Serial No to update: "))
                old_expense = manager.get_by_serial(serial_no)

                if not old_expense:
                    print("Expense not found.")
                    continue

                print("Leave field empty to keep current value")

                date_str = input("New Date (DD-MM-YYYY): ").strip()
                amount_str = input("New Amount: ").strip()
                category = input("New Category: ").strip()
                remark = input("New Remark: ").strip()

                new_date = date_str if date_str else old_expense.date
                new_amount = float(amount_str) if amount_str else old_expense.amount
                new_category = category.capitalize() if category else old_expense.category
                new_remark = remark if remark else old_expense.remark

                temp_expense = Expense(
                    serial_no=old_expense.serial_no,
                    date=new_date,
                    amount=new_amount,
                    category=new_category,
                    remark=new_remark
                )

                ok, err = validate_expense(temp_expense, manager.get_expenses(), is_update=True)
                if not ok:
                    print(err)
                    continue

                old_expense.date = new_date
                old_expense.amount = new_amount
                old_expense.category = new_category
                old_expense.remark = new_remark

                print("Expense updated successfully.")

            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                serial_no = int(input("Serial No to delete: "))
                deleted = manager.delete_expense(serial_no)
                print("Expense deleted." if deleted else "Expense not found.")
            except ValueError:
                print("Invalid serial number.")

        elif choice == "5":
            expenses = manager.get_expenses()
            if not expenses:
                print("No expenses to summarize.")
                continue

            while True:
                print("\n---- Summaries ----")
                print("1. Total Expense")
                print("2. Category Summary")
                print("3. Monthly Summary")
                print("4. Highest Expense")
                print("5. Lowest Expense")
                print("6. Back")

                sub = input("Choice: ").strip()

                if sub == "1":
                    print("Total:", summary.total_expense(expenses))

                elif sub == "2":
                    for k, v in summary.category_summary(expenses).items():
                        print(k, ":", v)

                elif sub == "3":
                    for k, v in summary.monthly_summary(expenses).items():
                        print(k, ":", v)

                elif sub == "4":
                    e = summary.highest_expense(expenses)
                    print(e.serial_no, e.amount, e.category)

                elif sub == "5":
                    e = summary.lowest_expense(expenses)
                    print(e.serial_no, e.amount, e.category)

                elif sub == "6":
                    break

                else:
                    print("Invalid choice.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")