# SQLite Database k liye Third Party library install nahi karni padti, ye python m inbuilt hota hai

from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Database ko connect karne k liye
conn = sqlite3.connect("test.db", check_same_thread=False)
# SQL Query ko run karega
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Todos(
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Completed TEXT
    )'''
)

# Query ko DB m save karne k liye
conn.commit()


@app.get('/')
def home():
    return{
        "message":"SQLite Connected"
    } 


#                   SQLite vs SQLAlchemy

# SQLAlchemy:
'''
Ye ORM hai 
SQL query use nahi hoti isme 
python code use hota hai and python se database handle hota hai
Large application and clean code 
'''
# SQLite:

'''
Isme SQL Query use hoti hai
Small application k liye use hota hai
ye inbuilt python m hota hai 
'''
