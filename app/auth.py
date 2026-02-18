USERS = {
    "admin": "admin123",
    "lakshay": "1234"
}

def login(username, password):
    return username in USERS and USERS[username] == password
