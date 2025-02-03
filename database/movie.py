import requests
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker

# API Configuration
API_URL = "https://www.freetestapi.com/api/v1/movies"

# SQLite and SQLAlchemy Configuration
db_path = 'sqlite:///movies.db'
engine = create_engine(db_path)
metadata = MetaData()

# Define Movies Table using SQLAlchemy
table_movies = Table('Movies', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('genre', String),
    Column('rating', Float),
    Column('release_date', String)
)
metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Fetch Movie/TV Show Data from API
def fetch_movie_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print("Failed to fetch data from API.")
        return []

# Store Data in SQLite using SQLAlchemy ORM
def store_movie_data(movies):
    session = Session()
    for movie in movies:
        movie_data = {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'genre': movie.get('genre', 'Unknown'),
            'rating': movie.get('rating', 0.0),
            'release_date': movie.get('release_date', 'N/A')
        }
        insert_stmt = table_movies.insert().values(**movie_data)
        try:
            session.execute(insert_stmt)
        except Exception as e:
            print(f"Error inserting data: {e}")
    session.commit()
    session.close()
    print("Movie data is stores successfully")
    
