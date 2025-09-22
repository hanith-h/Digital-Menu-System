import mysql.connector
from menu import view_menu

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="restaurant_db"
)
cursor = conn.cursor()

def place_order():
    order_items = []
    total_price = 0.0
    while True:
        item_id = input("Enter item ID to order (or press [ENTER] to finish): ")
        if item_id.lower() == '':
            break
        quantity = int(input("Enter quantity: "))
        cursor.execute("SELECT price FROM menu WHERE id = %s", (item_id,))
        price = float(cursor.fetchone()[0])
        order_items.append((item_id, quantity, price * quantity))
        total_price += price * quantity
        print(f"Added {quantity} x item ID {item_id} to order. Current total: ₹{total_price:.2f}")

    confirm = input("Confirm order? (yes/no): ").lower()
    if confirm == 'yes':
        for item in order_items:
            cursor.execute("INSERT INTO orders (item_id, quantity, status) VALUES (%s, %s, %s)", (item[0], item[1], 0))
        conn.commit()
        print("Order placed successfully.")
    else:
        print("Order cancelled.")

def close():
    conn.close()
