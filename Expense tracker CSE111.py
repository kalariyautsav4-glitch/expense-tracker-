import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


# ------------------ LOAD & SAVE DATA ------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------ ADD EXPENSE ------------------

def add_expense():
    amount = float(input("Enter amount: ₹ "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    note = input("Enter note/description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category.capitalize(),
        "note": note,
        "date": date
    }

    data = load_data()
    data.append(expense)
    save_data(data)

    print("\n✔ Expense added successfully!\n")


# ------------------ VIEW ALL EXPENSES ------------------

def view_expenses():
    data = load_data()

    if not data:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n------ All Expenses ------")
    for i, exp in enumerate(data, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")
    print()


# ------------------ CATEGORY SUMMARY ------------------

def category_summary():
    data = load_data()
    if not data:
        print("\nNo data available.\n")
        return

    summary = {}
    for exp in data:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n------ Category-wise Summary ------")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")
    print()


# ------------------ MONTHLY SUMMARY ------------------

def monthly_summary():
    data = load_data()
    if not data:
        print("\nNo expenses found.\n")
        return

    month = input("Enter month (YYYY-MM): ")

    total = 0
    print(f"\nExpenses for {month}:")
    for exp in data:
        if exp["date"].startswith(month):
            print(f"₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")
            total += exp["amount"]

    print(f"\nTotal spent in {month}: ₹{total}\n")


# ------------------ DELETE AN EXPENSE ------------------

def delete_expense():
    data = load_data()

    if not data:
        print("\nNo expenses to delete.\n")
        return

    view_expenses()
    item = int(input("Enter expense number to delete: "))

    if 1 <= item <= len(data):
        removed = data.pop(item - 1)
        save_data(data)
        print(f"\n✔ Deleted expense: ₹{removed['amount']} ({removed['category']})\n")
    else:
        print("\nInvalid choice.\n")


# ------------------ MAIN MENU ------------------

def main():
    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Delete an Expense")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("\nInvalid choice, try again.\n")


if __name__ == "__main__":
    main()
