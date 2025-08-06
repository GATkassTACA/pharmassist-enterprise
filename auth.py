import json
import os
import hashlib

USERS_FILE = "users.json"

def load_users():
    # TEMP: Hardcoded user for demo
    return {
        "kent": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd038bbf00a8fba89"
    }

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    users = load_users()
    hashed = hash_password(password)
    print("DEBUG: trying to log in as", username)
    print("DEBUG: expected hash", users.get(username))
    print("DEBUG: actual hash", hashed)
    return users.get(username) == hashed

def create_user(username, password):
    users = load_users()
    users[username] = hash_password(password)
    save_users(users)
