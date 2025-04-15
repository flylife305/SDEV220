
from sqlalchemy import create_engine, MetaData, Table, select

# Connect to the SQLite database
engine = create_engine('sqlite:///books.db')
connection = engine.connect()
metadata = MetaData()

# Reflect the existing 'books' table from the database
books = Table('books', metadata, autoload_with=engine)

# Select the title column and order by title
query = select(books.c.title).order_by(books.c.title)

# Execute the query and fetch results
results = connection.execute(query).fetchall()

# Print the titles
for row in results:
    print(row.title)

# Close the connection
connection.close()
