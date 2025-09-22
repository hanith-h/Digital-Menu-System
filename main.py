import mysql.connector
from admin import admin_login, total_sales, manage_menu, manage_orders, manage_users, close as admin_close
from chef import chef_login, chef_menu, close as chef_close
from customer import place_order, close as customer_close
from menu import view_menu

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="restaurant_db"
)
cursor = conn.cursor()

def main_menu():
    while True:
        print("\n1. Place Order")
        print("2. View Menu")
        print("3. Chef Login")
        print("4. Admin Login")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_menu()
            place_order()
        elif choice == '2':
            view_menu()
        elif choice == '3':
            if chef_login():
                chef_menu()
            else:
                print("Access Denied")
        elif choice == '4':
            if admin_login():
                while True:
                    print("\nAdmin Menu:")
                    print("1. Total Sales")
                    print("2. Manage Menu")
                    print("3. Manage Orders")
                    print("4. Manage Users")
                    print("5. Logout")
                    admin_choice = input("Enter choice: ")
                    if admin_choice == '1':
                        total_sales()
                    elif admin_choice == '2':
                        manage_menu()
                    elif admin_choice == '3':
                        manage_orders()
                    elif admin_choice == '4':
                        manage_users()
                    elif admin_choice == '5':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Access Denied")
        elif choice == '5':
            print('Thank you!')
            break
        else:
            print("Invalid choice. Please try again.")

    admin_close()
    chef_close()
    customer_close()

print("\n" + "*" * 60)
print(f"*{'WELCOME TO THE PROJECT OF DIGITAL MENU SYSTEM':^58}*")
print("*" * 60)
print(f"*{'Developed by:':^58}*")
print("*" + "-" * 58 + "*")
print(f"*{'Hanith Harid':^58}*")
print("*" * 60 + "\n")

main_menu()
