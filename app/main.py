from flask import Flask, request, render_template, redirect, url_for, make_response
import sqlite3
import jwt
import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('JWT_SECRET', 'mysecretkey')


# Initialize SQLite DB
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('login'))
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except:
            return redirect(url_for('login'))
        return f(current_user, *args, **kwargs)
    return decorated


@app.route("/")
def home():
    return "Flask App Running in Docker on GCP!"


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = None
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            error = "All fields are required"
        else:
            hashed_pw = generate_password_hash(password)
            try:
                conn = sqlite3.connect('db.sqlite3')
                c = conn.cursor()
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
                conn.commit()
                conn.close()
                message = "Signup successful! Please log in."
            except sqlite3.IntegrityError:
                error = "Username already exists"
    return render_template("signup.html", message=message, error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[0], password):
            token = jwt.encode({
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'], algorithm="HS256")
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('token', token)
            return resp
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)


@app.route("/dashboard")
@token_required
def dashboard(current_user):
    return render_template("dashboard.html", user=current_user)


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('token', '', expires=0)
    return resp


if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)