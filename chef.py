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

def chef_login():
    username = input("Enter chef username: ")
    password = input("Enter chef password: ")
    cursor.execute("SELECT * FROM chefs WHERE username = %s AND password = %s", (username, password))
    chef = cursor.fetchone()
    if chef:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def chef_menu():
    while True:
        print("\nChef Menu:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. View Menu")
        print("4. View Past Orders")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_orders()
        elif choice == '2':
            view_all_orders()
            order_id = int(input("Enter order ID to update: "))
            status = int(input("Enter new status (1 for being prepared, 2 for ready): "))
            update_order_status(order_id, status)
        elif choice == '3':
            view_menu()
        elif choice == '4':
            view_past_orders()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def view_orders():
    cursor.execute("""
        SELECT o.id, m.name, o.quantity, o.status
        FROM orders o JOIN menu m ON o.item_id = m.id
        WHERE o.status != 2 ORDER BY o.id
    """)
    orders = cursor.fetchall()
    print("\n<<< Orders >>>")
    print("{:<10} {:<20} {:<10} {:<10}".format("Order ID", "Item Name", "Quantity", "Status"))
    print("-" * 60)
    for order in orders:
        print("{:<10} {:<20} {:<10} {:<10}".format(order[0], order[1], order[2], order[3]))

def view_all_orders():
    cursor.execute("""
        SELECT o.id, m.name, o.quantity, o.status
        FROM orders o JOIN menu m ON o.item_id = m.id
        ORDER BY o.id
    """)
    orders = cursor.fetchall()
    print("\n<<< All Orders >>>")
    print("{:<10} {:<20} {:<10} {:<10}".format("Order ID", "Item Name", "Quantity", "Status"))
    print("-" * 60)
    for order in orders:
        print("{:<10} {:<20} {:<10} {:<10}".format(order[0], order[1], order[2], order[3]))

def view_past_orders():
    cursor.execute("""
        SELECT o.id, m.name, o.quantity, o.status
        FROM orders o JOIN menu m ON o.item_id = m.id
        WHERE o.status = 2
        ORDER BY o.id
    """)
    past_orders = cursor.fetchall()
    print("\n<<< Past Orders >>>")
    print("{:<10} {:<20} {:<10} {:<10}".format("Order ID", "Item Name", "Quantity", "Status"))
    print("-" * 60)
    for order in past_orders:
        print("{:<10} {:<20} {:<10} {:<10}".format(order[0], order[1], order[2], order[3]))

def update_order_status(order_id, status):
    cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (status, order_id))
    conn.commit()

def close():
    conn.close()
