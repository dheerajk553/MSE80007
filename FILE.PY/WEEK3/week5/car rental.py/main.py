from add_rental import add_rental
from process_payment import process_payment
import sqlite3

def view_available_cars():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Car WHERE is_available = 1")
    cars = cursor.fetchall()
    print("\nAvailable Cars:")
    for car in cars:
        print(f"Car ID: {car[0]}, Model: {car[1]}, Brand: {car[2]}, Price/Day: {car[3]}")
    conn.close()

def main():
    while True:
        print("\nWelcome to Kumar's Car Rental System")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Make a Payment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_cars()

        elif choice == "2":
            view_available_cars()
            try:
                customer_id = int(input("Enter Customer ID: "))
                car_id = int(input("Enter Car ID: "))
                rent_date = input("Enter Rent Date (YYYY-MM-DD): ")
                return_date = input("Enter Return Date (YYYY-MM-DD): ")
                add_rental(customer_id, car_id, rent_date, return_date)
            except ValueError:
                print("Invalid input. Please enter numeric values where required.")

        elif choice == "3":
            try:
                rental_id = int(input("Enter Rental ID: "))
                amount = float(input("Enter Payment Amount: "))
                method = input("Enter Payment Method (Online/Cash): ")
                process_payment(rental_id, amount, method)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
