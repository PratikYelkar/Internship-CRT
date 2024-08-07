import json
import os
from datetime import datetime

class BudgetTracker:
    def __init__(self, data_file='budget_data.json'):
        self.data_file = data_file
        self.transactions = []
        self.load_data() 

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.transactions = json.load(file)
        else:
            self.transactions = []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, type, category, amount):
        transaction = {
            'type': type,
            'category': category,
            'amount': amount,
            'date': str(datetime.now())
        }
        self.transactions.append(transaction)
        self.save_data()

    def calculate_budget(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expenses

    def analyze_expenses(self):
        categories = {}
        for t in self.transactions:
            if t['type'] == 'expense':
                if t['category'] not in categories:
                    categories[t['category']] = 0
                categories[t['category']] += t['amount']
        return categories

    def display_menu(self):
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                category = input("Enter income category: ")
                amount = float(input("Enter amount: "))
                self.add_transaction('income', category, amount)
            elif choice == '2':
                category = input("Enter expense category: ")
                amount = float(input("Enter amount: "))
                self.add_transaction('expense', category, amount)
            elif choice == '3':
                budget = self.calculate_budget()
                print(f"Remaining Budget: {budget}")
            elif choice == '4':
                expenses = self.analyze_expenses()
                for category, amount in expenses.items():
                    print(f"Category: {category}, Amount Spent: {amount}")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
