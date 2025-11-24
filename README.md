FinanceFlow is a simple command-line budget tracker written in Python that stores all your transactions in a CSV file for easy persistence and later analysis. It lets you add income and expenses, automatically maintains your running balance, and shows both summary and detailed transaction history.
________________________________________
Project overview
FinanceFlow is a lightweight terminal application for personal finance tracking.
It uses a CSV file (transactions.csv) to store transactions so your data persists between runs without requiring a database.
________________________________________
Features
•	Add income with description and amount.
•	Add expenses, automatically stored as negative amounts for simple balance calculation.
•	View a summary with:
o	Total income
o	Total expenses
o	Current balance (colored green for positive, red for negative in compatible terminals)
•	View a detailed, nicely formatted transaction history:
o	Date
o	Type (income/expense)
o	Description
o	Amount (with color and sign)
•	Automatic CSV persistence:
o	Automatically loads existing transactions at startup if transactions.csv exists.
o	Automatically saves every new transaction.
________________________________________

Requirements
•	Python 3.7 or later
•	No external dependencies (uses only the Python standard library: csv, os, datetime).
________________________________________
Usage
Run the application from the project directory:
bash
python main.py
# or
python3 main.py
You will see a menu like:
text
--- Budget Tracker Menu ---
1. Add Income
2. Add Expense
3. View Summary (Balance, Total Income/Expense)
4. View Detailed Transaction History
5. Exit
Enter a number from 1 to 5 to choose an action.
1. Add income
•	Choose option 1.
•	Enter a description (for example, Salary, Freelance, Gift).
•	Enter the income amount (positive number).
•	The app will:
o	Store the transaction as an income.
o	Use today’s date.
o	Save it immediately to transactions.csv.
2. Add expense
•	Choose option 2.
•	Enter a description (for example, Groceries, Rent, Transport).
•	Enter the expense amount (positive number).
•	The app will:
o	Store the transaction as an expense.
o	Convert the amount to a negative value internally for correct balance calculation.
o	Use today’s date.
o	Save it immediately to transactions.csv.
3. View summary
•	Choose option 3.
•	The app shows:
o	Total income (sum of all positive amounts).
o	Total expense (absolute value of sum of negative amounts).
o	Current balance (income + expenses), colored green if non negative and red if negative in terminals that support ANSI colors.
4. View detailed transaction history
•	Choose option 4.
•	The app prints all transactions sorted by date (newest first), with:
o	Index number
o	Date
o	Description
o	Type (INCOME / EXPENSE)
o	Amount, with a + or - sign and green/red coloring.
5. Exit
•	Choose option 5 to exit the application gracefully.
________________________________________
Data storage
•	The app uses a CSV file named transactions.csv in the project directory.
•	Columns:
o	date – date string in YYYY-MM-DD format
o	type – "income" or "expense"
o	name – text description of the transaction
o	amount – numeric value (positive for income, negative for expense)
•	On startup:
o	If transactions.csv exists, it is loaded into memory.
o	If it does not exist, the app starts with an empty list and creates the file when the first transaction is saved.
________________________________________
Customization ideas
You can extend FinanceFlow with:
•	Filtering transactions by date range or type.
•	Category support (e.g., Food, Rent, Entertainment).
•	Exporting monthly reports.
•	Graphs using libraries like matplotlib or pandas.
•	A GUI or web interface on top of the existing CSV logic.
________________________________________
Author
•	Name : Naman Jayesh Gundecha
•	Reg. No. : 25BCE10720
•	Mail : namangundecha22@gmail.com
•	GitHub : Naman Gundecha



