import psycopg2
import csv
import os
import sys
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="phonebook",
        user="postgres",
        password="123456"
    )

def init_db():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20)
                )
            """)
    print("Table created!")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Added!")

def insert_from_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    print("CSV imported!")

def update_phone(name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    print("Phone updated!")

def update_name(phone, new_name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
    print("Name updated!")

def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            for row in cur.fetchall():
                print(row)

def query_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
            print(cur.fetchall())

def query_by_phone(phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
            print(cur.fetchall())

def delete_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    print("Deleted by name!")

def delete_by_phone(phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    print("Deleted by phone!")

def menu():
    init_db()
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update phone")
        print("4. Update name")
        print("5. View all")
        print("6. Search by name")
        print("7. Search by phone")
        print("8. Delete by name")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("CSV path: "))
        elif choice == '3':
            update_phone(input("Name: "), input("New phone: "))
        elif choice == '4':
            update_name(input("Phone: "), input("New name: "))
        elif choice == '5':
            query_all()
        elif choice == '6':
            query_by_name(input("Name: "))
        elif choice == '7':
            query_by_phone(input("Phone: "))
        elif choice == '8':
            delete_by_name(input("Name: "))
        elif choice == '9':
            delete_by_phone(input("Phone: "))
        elif choice == '0':
            break

if __name__ == "__main__":
    menu()
