import psycopg2
import csv  

connection= psycopg2.connect(
    host="localhost",
    database="lab10bd",       
    user="postgres",         
    password="123456"   
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")

connection.commit()
print("Connected!")
print("Tables created!")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    connection.commit()

    print("Added!")

def insert_from_csv():
    path = input("Enter CSV file name: ")
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            read = csv.DictReader(csvfile)
            for row in read:
                cursor.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (row['name'], row['phone'])
                )
        connection.commit()
        print("Data imported from CSV!")
    except Exception as e:
        print("Error:", e)

def update_phone():
    name = input("Enter the name of the contact to update: ")
    new_phone = input("Enter the new phone number: ")
    cursor.execute("UPDATE contacts SET phone = %s WHERE name = %s", (new_phone, name))
    connection.commit()
    print(f"Updated phone number for {name}")

def update_name():
    phone = input("Enter the phone number of the contact to update: ")
    new_name = input("Enter the new name: ")
    cursor.execute("UPDATE contacts SET name = %s WHERE phone = %s", (new_name, phone))
    connection.commit()
    print(f"Updated name for phone {phone}")

def show_all_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    print("All contacts:")
    for row in rows:
        print(row)
def search_by_name():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))
    rows = cursor.fetchall()
    print(f"\nContacts matching '{name}':")
    for row in rows:
        print(row)
def search_by_phone():
    phone = input("Enter phone to search: ")
    cursor.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{phone}%",))
    rows = cursor.fetchall()
    print(f"\n Contacts matching '{phone}':")
    for row in rows:
        print(row)
def delete_by_name():
    name = input("Enter the name of the contact to delete: ")
    cursor.execute("DELETE FROM contacts WHERE name = %s", (name,))
    connection.commit()
    print(f"Contact with name '{name}' has been deleted.")
def delete_by_phone():
    phone = input("Enter the phone number of the contact to delete: ")
    cursor.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    connection.commit()
    print(f"Contact with phone '{phone}' has been deleted.")

while True:
    print("\n===== PhoneBook Menu =====")
    print("1. Add contact manually")
    print("2. Import from CSV file")
    print("3. Update phone number")
    print("4. Update name")
    print("5. Show all contacts")      
    print("6. Search by name")          
    print("7. Search by phone")          
    print("8. Delete by name")
    print("9. Delete by phone")
    print("0. Exit")

    choice = input("Select option: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        update_phone()
    elif choice == "4":
        update_name()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        search_by_name()
    elif choice == "7":
        search_by_phone()
    elif choice == "8":
        delete_by_name()
    elif choice == "9":
        delete_by_phone()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
cursor.close()
connection.close()
print("bye!")
