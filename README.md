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
Installation
1.	Clone this repository:
bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2.	Ensure you have Python 3 installed:
bash
python --version
# or
python3 --version
3.	(Optional but recommended) Create and activate a virtual environment:
bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
No additional packages need to be installed.
# Author :-
•	Name : Naman Jayesh Gundecha
•	Reg. No. : 25BCE10720
•	Mail : namangundecha22@gmail.com
•	GitHub : Naman Gundecha

