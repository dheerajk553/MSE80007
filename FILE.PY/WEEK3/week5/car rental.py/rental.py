import sqlite3

def add_rental(customer_id, car_id, rent_date, return_date):
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Rental (customer_id, car_id, rent_date, return_date)
        VALUES (?, ?, ?, ?)
    ''', (customer_id, car_id, rent_date, return_date))

    conn.commit()
    conn.close()
