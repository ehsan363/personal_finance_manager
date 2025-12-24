# Importing libraries
import sqlite3
from pathlib import Path
from dateAndTime import tdy

# Database path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "transactions"

class DBmanager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row # row_factory for better data handling

    def Expense(self):
        today = tdy()
        month = int(today.strftime('%m'))
        year = int(today.strftime('%Y'))

        cursor = self.conn.execute(f'''
            SELECT SUM(amount) AS total_expense
            FROM transactions
            WHERE type = 'expense'
            AND strftime('%Y', date) = '{year}'
            AND strftime('%m', date) = '{month}';''')
        rows = cursor.fetchall()
        totalExpense = float(f"{dict(rows[0])['total_expense']:.2f}")
        return totalExpense

    # Function for fetching transaction history
    def history(self):
        cursor = self.conn.execute('''
            SELECT category, amount, date, type
            FROM transactions
            ORDER BY date DESC
            LIMIT 5;''')
        rawRows = cursor.fetchall()
        rows = []
        data = []
        for i in rawRows:
            rows.append([dict(i)['category'],dict(i)['amount'],dict(i)['date'],dict(i)['type']])

        return rows

    # Function to close SQLite
    def close(self):
        conn.close()