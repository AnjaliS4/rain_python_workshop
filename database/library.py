# no 2 Task: Make a book library manager that stores books in SQLite.
# Use SQLAlchemy to add, remove, and search for books.
# Query books by genre, author, or rating
import 1
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base 

connection = sqlite3.connect("Store.db")
cursor = connection.cursor()

# create a table for Book  
cursor.execute('''CREATE TABLE IF NOT EXISTS Book ( 
    id INTEGER PRIMARY KEY,
    title STRING REQUIRED, 
    author STRING REQUIRED, 
    price FLOAT REQUIRED
)''')

cursor.execute("INSERT INTO Book (title, author, price) VALUES (?, ?, ?)", ("The Alchemist", "Paulo Coelho", 700.00))
cursor.execute("INSERT INTO Book (title, author, price) VALUES (?, ?, ?)", ("Midnight Library", "Matt Haig", 900.00))
cursor.execute("INSERT INTO Book (title, author, price) VALUES (?, ?, ?)", ("Normal People", "Salley rooney", 1200.00))

# fetch the dta 
cursor .execute("SELECT * FROM BOOK " )
for now in cursor.fetchall():
    print(now)

connection.close()

Books = session.query(Book).filter():
print(row)