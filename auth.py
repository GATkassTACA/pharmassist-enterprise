import hashlib

def load_users():
    return {
        "kent": "ff95c1631b1c2574910da9f96c353b92c27bb4d4f98ff96b59177981a5eb8c3b"
    }

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    users = load_users()
    hashed = hash_password(password)
    print("DEBUG: trying to log in as", username)
    print("DEBUG: expected hash", users.get(username))
    print("DEBUG: actual hash", hashed)
    return users.get(username) == hashed
