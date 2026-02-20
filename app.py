from flask import Flask, render_template, redirect, request, url_for
import sqlite3
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login_main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_main.html')

from flask import request, redirect, render_template

@app.route('/activity', methods=['GET', 'POST'])
def activity():

    conn = sqlite3.connect("progresso.db")
    cursor = conn.cursor()

    # If user submits form
    if request.method == "POST":
        points = request.form["points"]
        cursor.execute("INSERT INTO activity (points) VALUES (?)", (points,))
        conn.commit()

    # Get total points
    cursor.execute("SELECT SUM(points) FROM activity")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    conn.close()

    return render_template("activity_point_main.html", total=total)

@app.route('/assignment')
def assignment():
    return render_template('assignment_main.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses_main.html')

@app.route('/study')
def study():
    return render_template('study_main.html')

@app.route('/profile')
def profile():
    return render_template('profile_main.html')

@app.route('/settings')
def settings():
    return render_template('settings_main.html')

@app.route('/logout')
def logout():
    return redirect(url_for('home'))
if __name__ == "__main__":

    conn = sqlite3.connect("progresso.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            points INTEGER
        )
    """)

    conn.commit()
    conn.close()

    app.run(debug=True)
    