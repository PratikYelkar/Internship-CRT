# Personal Budget Tracker

A console-based budget tracker that allows users to manage their expenses and income, calculate their remaining budget, analyze expenses, and persist data in a file.

## Features

1. **Expense and Income Entry:** Allow users to input expenses and income with categories and amounts.
2. **Budget Calculation:** Calculate the remaining budget after deducting expenses from income.
3. **Expense Analysis:** Provide insights by categorizing expenses and displaying spending trends.
4. **Data Persistence:** Store transactions in a JSON file for tracking over time.

## Requirements

- Python 3.x

## Run the Script

python budget_tracker.py

Usage

When you run the script, you will see a menu with the following options:

1. Add Income
2. Add Expense
3. View Budget
4. Analyze Expenses
5. Exit


Example Interaction :

1. Add Income:
Choose an option: 1
Enter income category: Salary
Enter amount: 3000

2. Add Expense:
Choose an option: 2
Enter expense category: Rent
Enter amount: 1000

3. Add Another Expense:
Choose an option: 2
Enter expense category: Groceries
Enter amount: 200

4. View Budget:
Choose an option: 3
Remaining Budget: 1800

5. Analyze Expenses:
Choose an option: 4
Category: Rent, Amount Spent: 1000
Category: Groceries, Amount Spent: 200

6. Exit:
Choose an option: 5

Data Persistence
All transactions are stored in a file named budget_data.json in the same directory as the script. This allows the program to track income and expenses across sessions.
