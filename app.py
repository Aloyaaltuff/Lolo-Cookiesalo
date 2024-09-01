from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from basemode import add_user, authenticate
import json

app = Flask(__name__)
app.secret_key = 'alo0987667890'


def load_users():
    """Load users from a JSON file."""
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save users to a JSON file."""
    with open('users.json', 'w') as f:
        json.dump(users, f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            flash('Login successful!', 'success')
            return redirect('index.html')
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Username and password are required.', 'error')
        else:
            add_user(username, password)
            flash('Registration successful! Please log in.', 'success')
            return redirect('login.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500,debug=True)

