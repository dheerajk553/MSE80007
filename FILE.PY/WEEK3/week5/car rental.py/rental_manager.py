import sqlite3
from payment import process_payment

def add_rental(customer_id, car_id, rent_date, return_date):
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    # Example logic: mark car as rented
    cursor.execute("UPDATE Car SET is_available = 0 WHERE car_id = ?", (car_id,))
    
    # You can expand this to insert into Rental table later
    print(f"Car {car_id} rented on {rent_date}")

    conn.commit()
    conn.close()

    def process_payment(rental_id, amount, method):
       conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Payment (rental_id, amount, method)
        VALUES (?, ?, ?)
    """, (rental_id, amount, method))

    conn.commit()
    conn.close()
    print(f"Payment of ${amount} recorded for Rental ID {rental_id} via {method}")

