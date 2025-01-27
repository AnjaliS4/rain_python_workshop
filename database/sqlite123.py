# Using SQLite3 to interact with a database 
import sqlite3
connection = sqlite3.connect("Store.db")
cursor = connection.cursor()

# create a table for products 
cursor.execute('''CREATE TABLE IF NOT EXISTS products ( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)''')

#Insert Data 
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Laptop", 999.99))
connection.commit()

# Fetch Data 
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

connection.close()

# Using AQLAlchemy for database interaction 