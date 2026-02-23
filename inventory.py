import sqlite3
import os

def init_database():
    """Initializes the database and creates the table if it doesn't exist."""
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCTS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            CATEGORY TEXT,
            QUANTITY INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_product():
    """Gets user input and adds a new product to the database."""
    name = input("Product Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO PRODUCTS(NAME, CATEGORY, QUANTITY)
                   
        VALUES (?, ?, ?)
    ''', (name, category, quantity))
    conn.commit()
    conn.close()
    print(f"\n[+] {name} successfully added.")

def list_products():
    """Displays all products from the database."""
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PRODUCTS')
    items = cursor.fetchall()
    conn.close()

    print("\n CURRENT INVENTORY ")
    print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Quantity':<10}")
    print("-" * 60)
    for item in items:
        print(f"{item[0]:<5} {item[1]:<20} {item[2]:<15} {item[3]:<10}")

def delete_product():
    """Deletes a product"""
    product_id = input("\nEnter the ID of the product: ")
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM PRODUCTS WHERE ID = ?', (product_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"\n[-] Product ID {product_id} deleted.")
    else:
        print("\n[!] Product ID not found.")
    conn.close()

# MAIN MENU

def main_menu():
    init_database()
    while True:
        print("\n INVENTORY MANAGEMENT SYSTEM ")
        print("1. List Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            list_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
