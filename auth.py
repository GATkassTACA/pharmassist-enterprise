
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
