import sqlite3
import time

class UserService:
    def get_user(self, user_id):
        start = time.time()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        end = time.time()
        print("User query time: {:.4f} seconds".format(end - start))
        return user

class OrderService:
    def get_orders(self, user_id):
        start = time.time()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        conn.close()
        end = time.time()
        print("Order query time: {:.4f} seconds".format(end - start))
        return orders
