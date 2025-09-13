import sqlite3
import time

def get_user(user_id):
    start = time.time()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    cursor.fetchone()
    conn.close()
    end = time.time()
    print("User query time: {:.4f} seconds".format(end - start))

def get_orders(user_id):
    start = time.time()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
    cursor.fetchall()
    conn.close()
    end = time.time()
    print("Order query time: {:.4f} seconds".format(end - start))

if __name__ == "__main__":
    user_id = 1
    get_user(user_id)
    get_orders(user_id)
