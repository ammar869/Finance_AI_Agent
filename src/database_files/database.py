import sqlite3

connection = sqlite3.connect("finance.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    description TEXT,
    amount REAL
)
""")

cursor.execute("""
INSERT INTO transactions
(date, category, description, amount)
VALUES
('2026-08-01', 'Food', 'Lunch', 500),
('2026-08-02', 'Transport', 'Uber', 800),
('2026-08-03', 'Food', 'Dinner', 700),
('2026-08-04', 'Shopping', 'Shoes', 5000),
('2026-08-05', 'Food', 'Breakfast', 300)
""")

connection.commit()
connection.close()