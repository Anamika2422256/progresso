import sqlite3

def init_db():
    conn = sqlite3.connect("progresso.db")
    cursor = conn.cursor()

    # Activity Points
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            points INTEGER
        )
    """)

    # Assignments
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            due_date TEXT
        )
    """)

    # Expenses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL
        )
    """)

    conn.commit()
    conn.close()