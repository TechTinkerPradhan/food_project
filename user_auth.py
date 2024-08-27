import sqlite3
import hashlib
import json
import os 

def create_user(user_id, password):
    conn = sqlite3.connect("/home/artemis/foodproject/food_rec_bot/data/app.db")
    cursor = conn.cursor()
    
    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Insert the new user
    cursor.execute("INSERT INTO users (user_id, password) VALUES (?, ?)", (user_id, hashed_password))
    conn.commit()
    conn.close()

def login_user(user_id, password):
    conn = sqlite3.connect("/home/artemis/foodproject/food_rec_bot/data/app.db")
    cursor = conn.cursor()
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute("SELECT * FROM users WHERE user_id=? AND password=?", (user_id, hashed_password))
    result = cursor.fetchone()
    conn.close()
    
    return result is not None

def load_user_preferences(user_id):
    file_path = f"/home/artemis/foodproject/food_rec_bot/data/user_preferences/{user_id}_preferences.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []

def save_user_preferences(user_id, preferences):
    file_path = f"/home/artemis/foodproject/food_rec_bot/data/user_preferences/{user_id}_preferences.json"
    with open(file_path, "w") as file:
        json.dump(preferences, file)
