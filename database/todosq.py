# discription: Design a simple to-do list with an SQL database.
# Create a table for discriptions (ID, description, due date).
# Allow users to add, remove, and view discriptions.

import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

Base = declarative_base() # skema 

class Todolist(Base):
    __tablename__ = 'Todolist'
    id = Column(Integer, primary_key=True)
    discription = Column(String, nullable=False)
    duedate = Column(date, nullable=False)

# Create  engine and session 
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class TodoList:
    def __init__(self):
        self.discriptions = []

    def add_discription(self,discription):
        self.discriptions.append(discription)
        print(f"'{discription}'added to the list")

    def remove_discription(self.discription):
        if discription in self.discriptions:
            self.discriptions.remove(discription)
            print("fdiscription'{discription}'removed from the list")
        else:
            print(f"discription'{discription}' not found in the list")
    def update_discription(self, old_discription, new_discription):
        if old_discription in self.discriptions:
            index = self.discriptions.index(old_discription)
            self.discriptions[index] = new_discription
            print(f"discription updated to '{new_discription}'.")
        else:
            print(f"discription'{old_discription}' not found in list")
    def show_discriptions(self):
        if self.discriptions:
            print("your todo list")
            for index, discription in enumerate(self.discriptions):
                print(f"{index + 1 }. {discription}")
        else:
            print("your todo list is empty.")



