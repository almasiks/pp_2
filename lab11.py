import psycopg2
import csv
import os
import sys

if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
import psycopg2

DB_CONFIG = {
    'host': "127.0.0.1",  
    'dbname': "phonebook_2",
    'user': "postgres",
    
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Подключение успешно!")
    conn.close()
except psycopg2.Error as e:
    print("Ошибка подключения:", e)

def connect():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook_2 (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20)
                )
            """)
            
            cur.execute("""
                CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
                RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY
                    SELECT p.id, p.name, p.phone
                    FROM phonebook_2 p
                    WHERE p.name ILIKE '%' || pattern || '%'
                       OR p.phone LIKE '%' || pattern || '%';
                END;
                $$ LANGUAGE plpgsql;
            """)
            
            cur.execute("""
                CREATE OR REPLACE PROCEDURE upsert_user(user_name VARCHAR, user_phone VARCHAR)
                LANGUAGE plpgsql AS $$
                BEGIN
                    IF EXISTS (SELECT 1 FROM phonebook_2 WHERE name = user_name) THEN
                        UPDATE phonebook_2 SET phone = user_phone WHERE name = user_name;
                    ELSE
                        INSERT INTO phonebook_2 (name, phone) VALUES (user_name, user_phone);
                    END IF;
                END;
                $$;
            """)
            
            cur.execute("""
                CREATE TABLE IF NOT EXISTS invalid_phones (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20),
                    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cur.execute("""
                CREATE OR REPLACE PROCEDURE bulk_insert_users(names TEXT[], phones TEXT[])
                LANGUAGE plpgsql AS $$
                DECLARE
                    i INT;
                BEGIN
                    FOR i IN 1..array_length(names, 1)
                    LOOP
                        IF phones[i] ~ '^[0-9+\\-\\(\\) ]{7,20}$' THEN
                            INSERT INTO phonebook_2 (name, phone) VALUES (names[i], phones[i]);
                        ELSE
                            INSERT INTO invalid_phones (name, phone) VALUES (names[i], phones[i]);
                        END IF;
                    END LOOP;
                END;
                $$;
            """)
            
            cur.execute("""
                CREATE OR REPLACE FUNCTION paginate_phonebook(page_limit INT, page_offset INT)
                RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY
                    SELECT p.id, p.name, p.phone
                    FROM phonebook_2 p
                    ORDER BY p.id
                    LIMIT page_limit OFFSET page_offset;
                END;
                $$ LANGUAGE plpgsql;
            """)
            
            cur.execute("""
                CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(pattern VARCHAR)
                LANGUAGE plpgsql AS $$
                BEGIN
                    DELETE FROM phonebook_2 WHERE name = pattern OR phone = pattern;
                END;
                $$;
            """)
    print("Database initialized with all functions and procedures!")

def search_pattern(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            return cur.fetchall()

def upsert_user(name: str, phone: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    print(f"Upserted user: {name} -> {phone}")

def bulk_insert(names: list[str], phones: list[str]):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_users(%s, %s)", (names, phones))
    print("Bulk insert complete. Invalid phones logged in 'invalid_phones' table.")

def paginated_view(limit: int, offset: int):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
            return cur.fetchall()

def delete_by_name_or_phone(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by_name_or_phone(%s)", (pattern,))
    print(f"Deleted records matching: {pattern}")

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    upsert_user(name, phone)

def insert_from_csv(path: str):
    names, phones = [], []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                names.append(row[0])
                phones.append(row[1])
    bulk_insert(names, phones)

def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_2 ORDER BY id")
            return cur.fetchall()

def query_by_name(name: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_2 WHERE name = %s", (name,))
            return cur.fetchall()

def view_invalid_phones():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM invalid_phones ORDER BY logged_at DESC")
            return cur.fetchall()

def menu():
    init_db()
    
    while True:
        print("\n" + "="*50)
        print("        PHONEBOOK MENU")
        print("="*50)
        print("1. Insert single user (console)")
        print("2. Bulk insert from CSV")
        print("3. Upsert user")
        print("4. Search by pattern (function)")
        print("5. View paginated (function)")
        print("6. Delete by name or phone (procedure)")
        print("7. Show all contacts")
        print("8. View invalid phones log")
        print("0. Exit")
        print("="*50)
        
        choice = input("Enter choice: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("CSV file path: "))
        elif choice == '3':
            upsert_user(input("Name: "), input("Phone: "))
        elif choice == '4':
            results = search_pattern(input("Pattern: "))
            if results:
                for row in results:
                    print(row)
            else:
                print("No results found")
        elif choice == '5':
            try:
                limit = int(input("Limit: "))
                offset = int(input("Offset: "))
                results = paginated_view(limit, offset)
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No more records")
            except ValueError:
                print("Invalid input for limit/offset")
        elif choice == '6':
            delete_by_name_or_phone(input("Name or phone to delete: "))
        elif choice == '7':
            results = query_all()
            if results:
                for row in results:
                    print(row)
            else:
                print("No contacts")
        elif choice == '8':
            results = view_invalid_phones()
            if results:
                print("\nInvalid phones log:")
                for row in results:
                    print(row)
            else:
                print("No invalid phones logged")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()  
