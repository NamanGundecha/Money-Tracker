import csv
import os
from datetime import datetime

class BudgetTracker:
    """
    A command-line budget tracking application that loads and saves
    transaction data to a CSV file.
    """
    def __init__(self, filename="transactions.csv"):
        """Initializes the tracker and attempts to load existing data."""
        self.filename = filename
        self.transactions = []
        self._load_data()

    def _load_data(self):
        """Loads transactions from the CSV file."""
        if not os.path.exists(self.filename):
            print(f"[{self.filename}] not found. Starting with an empty budget.")
            return

        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert amount back to float and ensure date is included
                    try:
                        row['amount'] = float(row['amount'])
                        # Use the stored string date, or default to today if missing
                        row['date'] = row.get('date', datetime.now().strftime('%Y-%m-%d'))
                        self.transactions.append(row)
                    except ValueError:
                        print(f"Skipping malformed transaction row: {row}")
            print(f"Successfully loaded {len(self.transactions)} transactions.")
        except Exception as e:
            print(f"Error loading data from {self.filename}: {e}")

    def _save_data(self):
        """Saves all current transactions back to the CSV file."""
        try:
            fieldnames = ['date', 'type', 'name', 'amount']
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.transactions)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_transaction(self, t_type, name, amount):
        """
        Adds a new transaction. Expenses are stored as negative amounts.
        
        :param t_type: 'income' or 'expense'.
        :param name: Description of the transaction.
        :param amount: The value of the transaction (positive).
        """
        if amount <= 0:
            print("Error: Amount must be positive.")
            return

        # Convert expense to negative for balance calculation
        if t_type.lower() == 'expense':
            amount = -amount

        new_transaction = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'type': t_type.lower(),
            'name': name.strip(),
            'amount': amount
        }
        self.transactions.append(new_transaction)
        self._save_data()
        print(f"\n--- {t_type.upper()} added successfully! ---")

    def calculate_balance(self):
        """Calculates and returns the current total balance."""
        return sum(t['amount'] for t in self.transactions)

    def display_summary(self):
        """Displays the current balance and a breakdown of total income and expenses."""
        total_balance = self.calculate_balance()
        total_income = sum(t['amount'] for t in self.transactions if t['amount'] > 0)
        total_expense = sum(t['amount'] for t in self.transactions if t['amount'] < 0)

        print("\n" + "="*40)
        print("         FINANCE FLOW SUMMARY")
        print("="*40)
        print(f"Total Income:  ${total_income:,.2f}")
        print(f"Total Expense: ${abs(total_expense):,.2f}")
        print("-" * 40)
        
        balance_sign = "+" if total_balance >= 0 else "-"
        balance_color = "\033[92m" if total_balance >= 0 else "\033[91m" # Green or Red terminal color
        print(f"Current Balance: {balance_color}{balance_sign}${abs(total_balance):,.2f}\033[0m")
        print("="*40 + "\n")


    def display_transactions(self):
        """Prints a detailed list of all recorded transactions."""
        if not self.transactions:
            print("\nNo transactions recorded yet.")
            return

        print("\n" + "#"*50)
        print("             TRANSACTION HISTORY")
        print("#"*50)
        
        # Sort by date descending for display
        sorted_transactions = sorted(self.transactions, key=lambda x: x['date'], reverse=True)

        for i, t in enumerate(sorted_transactions):
            amount_display = f"${abs(t['amount']):,.2f}"
            
            if t['amount'] > 0:
                color = "\033[92m"  # Green
                sign = "+"
            else:
                color = "\033[91m"  # Red
                sign = "-"
            
            print(f"{i+1:02}. [{t['date']}] {t['name']:<25} | {t['type'].upper():<7} | {color}{sign}{amount_display:<10}\033[0m")
        
        print("#"*50 + "\n")


def get_float_input(prompt):
    """Helper function to safely get a positive float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Main function to run the command-line interface."""
    tracker = BudgetTracker()

    while True:
        print("\n\n--- Budget Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary (Balance, Total Income/Expense)")
        print("4. View Detailed Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- ADD INCOME ---")
            name = input("Enter income description (e.g., Salary, Gift): ")
            amount = get_float_input("Enter income amount: ")
            tracker.add_transaction('income', name, amount)

        elif choice == '2':
            print("\n--- ADD EXPENSE ---")
            name = input("Enter expense description (e.g., Groceries, Rent): ")
            amount = get_float_input("Enter expense amount: ")
            tracker.add_transaction('expense', name, amount)
            
        elif choice == '3':
            tracker.display_summary()
            
        elif choice == '4':
            tracker.display_transactions()

        elif choice == '5':
            print("Thank you for using FinanceFlow! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
