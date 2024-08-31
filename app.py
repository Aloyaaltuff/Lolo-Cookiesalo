from flask import Flask, request, render_template, redirect, url_for, session, flash
import bcrypt
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
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

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def authenticate(username, password):
    """Authenticate a user with hashed password."""
    users = load_users()
    hashed_password = users.get(username)
    return hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.route('/')
def home():
    """Render the home page."""
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            flash('User already exists!')
            return redirect(regester.html)
        hashed_password = hash_password(password)
        users[username] = hashed_password
        save_users(users)
        flash('User registered successfully!')
        return redirect(login.html)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            session['username'] = username
            flash('Login successful!')
            return redirect(index.html)
        flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(login.html)

if __name__ == '__main__':
    app.run(debug=True)
