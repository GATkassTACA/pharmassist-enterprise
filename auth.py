import hashlib

def load_users():
    return {
        "kent": "import hashlib
print(hashlib.sha256("KentPassword123".encode()).hexdigest())
8c3b"
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
