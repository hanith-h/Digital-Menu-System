import mysql.connector
from menu import view_menu

# Connection to SQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="restaurant_db"
)
cursor = conn.cursor()

# Function for admin login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    cursor.execute("SELECT * FROM admins WHERE username = %s AND password = %s", (username, password))
    admin = cursor.fetchone()
    if admin:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

# Function to calculate total sales
def total_sales():
    cursor.execute("""
        SELECT SUM(m.price * o.quantity)
        FROM orders o JOIN menu m ON o.item_id = m.id
        WHERE o.status = 2
    """)
    total = cursor.fetchone()[0] or 0
    print(f'Total sales: ₹{total:.2f}')

# Function to manage the menu
def manage_menu():
    while True:
        print("\n>>> Manage Menu <<<")
        print("1. Add item to menu")
        print("2. Remove item from menu")
        print("3. Update item quantity")
        print("4. View menu")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item_to_menu()
            view_menu()
        elif choice == '2':
            view_menu()
            remove_item_from_menu()
            view_menu()
        elif choice == '3':
            update_item_quantity()
            view_menu()
        elif choice == '4':
            view_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cursor.execute("INSERT INTO menu (name, price, quantity) VALUES (%s, %s, %s)", (name, price, 0))
    conn.commit()

def remove_item_from_menu():
    item_id = int(input("Enter item ID to remove: "))
    cursor.execute("DELETE FROM orders WHERE item_id = %s", (item_id,))
    conn.commit()
    cursor.execute("DELETE FROM menu WHERE id = %s", (item_id,))
    conn.commit()
    print(f"Item {item_id} and its related orders have been deleted successfully.")

def update_item_quantity():
    item_id = int(input("Enter item ID to update quantity: "))
    new_quantity = int(input("Enter new quantity: "))
    cursor.execute("UPDATE menu SET quantity = %s WHERE id = %s", (new_quantity, item_id))
    conn.commit()
    print(f"Updated item {item_id} quantity to {new_quantity}.")

# Function to manage orders
def manage_orders():
    while True:
        print("1. View all orders")
        print("2. Update order status")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_all_orders()
        elif choice == '2':
            order_id = int(input("Enter order ID to update: "))
            status = int(input("Enter new status (1 for being prepared, 2 for ready): "))
            update_order_status(order_id, status)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def view_all_orders():
    cursor.execute("""
        SELECT o.id, m.name, o.quantity, o.status
        FROM orders o JOIN menu m ON o.item_id = m.id
        ORDER BY o.id
    """)
    orders = cursor.fetchall()
    print("\n--- All Orders ---")
    print(f"{'Order ID':<10} {'Item Name':<20} {'Quantity':<10} {'Status':<10}")
    print("-" * 60)
    for order in orders:
        print(f"{order[0]:<10} {order[1]:<20} {order[2]:<10} {order[3]:<10}")

def update_order_status(order_id, status):
    cursor.execute("UPDATE orders SET status=%s WHERE id=%s", (status, order_id))
    conn.commit()

# Function to manage users
def manage_users():
    while True:
        print("\n--- Manage Users ---")
        print("1. Add User")
        print("2. View Usernames")
        print("3. Delete User")
        print("4. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_user()
            view_usernames()
        elif choice == '2':
            view_usernames()
        elif choice == '3':
            delete_user()
            view_usernames()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user():
    while True:
        print("\n--- Add User ---")
        print("1. Add Admin")
        print("2. Add Chef")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_admin()
        elif choice == '2':
            add_chef()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_admin():
    username = input("Enter new admin username: ")
    password = input("Enter new admin password: ")
    cursor.execute("INSERT INTO admins (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print(f"Admin {username} added successfully.")

def add_chef():
    username = input("Enter new chef username: ")
    password = input("Enter new chef password: ")
    cursor.execute("INSERT INTO chefs (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print(f"Chef {username} added successfully.")

def view_usernames():
    print("\n--- Admins ---")
    cursor.execute("SELECT username FROM admins")
    admins = cursor.fetchall()
    for admin in admins:
        print(admin[0])
    print("\n--- Chefs ---")
    cursor.execute("SELECT username FROM chefs")
    chefs = cursor.fetchall()
    for chef in chefs:
        print(chef[0])

def delete_user():
    while True:
        print("\n--- Delete User ---")
        print("1. Delete Admin")
        print("2. Delete Chef")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            delete_admin()
        elif choice == '2':
            delete_chef()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def delete_admin():
    username = input("Enter admin username to delete: ")
    cursor.execute("DELETE FROM admins WHERE username = %s", (username,))
    conn.commit()
    print(f"Admin {username} deleted successfully.")

def delete_chef():
    username = input("Enter chef username to delete: ")
    cursor.execute("DELETE FROM chefs WHERE username = %s", (username,))
    conn.commit()
    print(f"Chef {username} deleted successfully.")

def close():
    conn.close()
