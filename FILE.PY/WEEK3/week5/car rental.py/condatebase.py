import sqlite3
#Connect to Database
conn = sqlite3.connect('car_rental.db')  # Creates or opens the database file
cursor = conn.cursor()
# Create Customer table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    phone TEXT,
    address TEXT,
    dl_number TEXT,
    dl_expiry_date TEXT
)
''')

# Create Car table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Car (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model_year INTEGER,
    mileage REAL,
    color TEXT,
    rent_per_week REAL,
    is_available BOOLEAN
)
''')

# Create Rental table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Rental (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    car_id INTEGER,
    rent_date TEXT,
    return_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (car_id) REFERENCES Car(car_id)
)
''')

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
