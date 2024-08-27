import sqlite3

def create_connection():
    conn = sqlite3.connect("data/app.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        user_id TEXT PRIMARY KEY,
                        password TEXT NOT NULL
                    )""")
    
    conn.commit()
    conn.close()

def insert_user(user_id, password):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (user_id, password) VALUES (?, ?)", (user_id, password))
    conn.commit()
    conn.close()
