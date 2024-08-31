import json
import os
import getpass

USERS_FILE = 'users.json'

def load_users():
    """Load users from a JSON file."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to a JSON file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def add_user(username, password):
    """Add a new user."""
    users = load_users()
    if username in users:
        print(f'User "{username}" already exists.')
    else:
        users[username] = password
        save_users(users)
        print(f'User "{username}" added.')

def authenticate(username, password):
    """Authenticate a user."""
    users = load_users()
    if users.get(username) == password:
        return True
    return False

def register_user():
    """Register a new user."""
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    add_user(username, password)

def login_user():
    """Log in a user."""
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    if authenticate(username, password):
        print('Login successful.')
        return True
    else:
        print('Invalid username or password.')
        return False

