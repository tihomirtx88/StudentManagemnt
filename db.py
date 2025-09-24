import sqlite3

DB_PATH = "database.db"

def get_all_students():
    conn = sqlite3.connect(DB_PATH)
    result = conn.execute("SELECT * FROM students")
    rows = list(result)
    conn.close()
    return rows

def insert_student(name, course, mobile):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                   (name, course, mobile))
    conn.commit()
    cursor.close()
    conn.close()

def search_students_by_name(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    rows = list(result)
    cursor.close()
    conn.close()
    return rows