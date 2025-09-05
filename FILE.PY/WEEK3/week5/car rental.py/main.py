from add_rental import add_rental
from process_payment import process_payment
import sqlite3

def view_available_cars():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Car WHERE is_available = 1")
    cars = cursor.fetchall()
    for car in cars:
        print(car)
    conn.close()

def main():
    print("Welcome to Kumar's Car Rental System")
    print("1. Rent a Car")
    print("2. Make a Payment")
    print("3. Exit")

    choice = input("Enter your choice: ")

    choice = input("Enter your choice: ")
    if choice == "1":
        customer_id = int(input("Enter Customer ID: "))
        car_id = int(input("Enter Car ID: "))
        rent_date = input("Enter Rent Date (YYYY-MM-DD): ")
        return_date = input("Enter Return Date (YYYY-MM-DD): ")

        add_rental(customer_id, car_id, rent_date, return_date)

    elif choice == "2":
        rental_id = int(input("Enter Rental ID: "))
        amount = float(input("Enter Payment Amount: "))
        method = input("Enter Payment Method (Online/Cash): ")

        process_payment(rental_id, amount, method)

    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()