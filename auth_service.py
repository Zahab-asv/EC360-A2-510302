import hashlib

users = {}

def register(email, password):
    if email in users:
        return False
    users[email] = hashlib.sha256(password.encode()).hexdigest()
    return True
