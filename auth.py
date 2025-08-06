def load_users():
    return {
        "kent": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd038bbf00a8fba89"
    }
import json
import os
import hashlib

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    users = load_users()
    return users.get(username) == hash_password(password)

def create_user(username, password):
    users = load_users()
    users[username] = hash_password(password)
    save_users(users)
