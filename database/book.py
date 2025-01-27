# id title author pricce 
import sqlite3
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



# Fetch Data 
cursor.execute("SELECT * FROM Book")
for row in cursor.fetchall():
    print(row)

connection.close()

Books = session.query(Book).filter( 
	and_(Book.title == "Alchemist"))
for Book in Books: 
	print(Book.name) 

connection.commit()


# cannot merge session and cursor 