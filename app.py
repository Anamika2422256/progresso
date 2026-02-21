from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('progresso.db')
    # Create the Activity Table (Participation Logs)
    conn.execute('''CREATE TABLE IF NOT EXISTS activity 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     name TEXT, category TEXT, date TEXT, points INTEGER)''')
    conn.commit()
    conn.close()

# --- ROUTES ---

@app.route('/')
def login_page():
    return render_template('login_main.html')

@app.route('/login', methods=['POST'])
def login():
    # Simple redirect to simulate login
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('progresso.db')
    # Fetch total points for the summary card
    row = conn.execute('SELECT SUM(points) FROM activity').fetchone()
    total = row[0] if row[0] else 0
    conn.close()
    return render_template('dashboard_main.html', total=total)

@app.route('/activity', methods=['GET', 'POST'])
def activity():
    conn = sqlite3.connect('progresso.db')
    conn.row_factory = sqlite3.Row # This allows using log['name'] in HTML
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('activity_name')
        pts = request.form.get('points')
        dt = request.form.get('date')
        cat = request.form.get('category', 'General') # Default if empty
        
        if name and pts:
            cursor.execute("INSERT INTO activity (name, category, date, points) VALUES (?, ?, ?, ?)", 
                           (name, cat, dt, pts))
            conn.commit()

    # Get all logs to display in the table
    logs = cursor.execute("SELECT * FROM activity ORDER BY id DESC").fetchall()
    
    # Calculate total points
    total_result = cursor.execute("SELECT SUM(points) FROM activity").fetchone()
    total = total_result[0] if total_result[0] is not None else 0
    
    conn.close()
    return render_template("activity_point_main.html", total=total, logs=logs)

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
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)