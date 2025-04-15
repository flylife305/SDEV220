import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'books' table with 'title', 'author', and 'year' columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
# Function to add a book to the database

