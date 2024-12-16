import sqlite3

def create_db():
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()

    # Create a table for storing user credentials
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Run the function to create the database and table
create_db()
