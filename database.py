import os
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'linkkiwi2026'  # needed for flash messages

#Absoulite path - Always with app1.py folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'myproject.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS SCORE (
            Sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_name TEXT NOT NULL,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            subject TEXT NOT NULL,
            score INTEGER NOT NULL,
            time TEXT NOT NULL 
        )
    ''')

    try:
        conn.execute("ALTER TABLE SCORE add column role text default 'student'")
    except Exception:
        pass



    conn.execute("""
    CREATE TABLE IF NOT EXISTS QUESTIONS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,         
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    """)

    conn.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")
    
    default_subjects = ['java','cpp','python','Operating System','Data Science','Database Management']
    
    for subject in default_subjects:
        try:
            conn.execute("INSERT INTO subjects (name) VALUES (?)", (subject,))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()

init_db()  # function call
if __name__ == "__main__":
    
    app.run(debug=True)