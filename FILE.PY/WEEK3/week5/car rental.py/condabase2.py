# condabase2.py
import sqlite3
conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

# Create Payment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rental_id INTEGER,
    amount REAL,
    method TEXT,
    FOREIGN KEY (rental_id) REFERENCES Rental(rental_id)
)
''')

conn.commit()
conn.close()
