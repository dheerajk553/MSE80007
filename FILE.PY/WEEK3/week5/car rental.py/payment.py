import sqlite3

def process_payment(rental_id, amount, method):
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Payment (rental_id, amount, method)
        VALUES (?, ?, ?)
    """, (rental_id, amount, method))

    conn.commit()
    conn.close()
    print(f"Payment of ${amount} recorded for Rental ID {rental_id} via {method}")
