import sqlite3

# Connect to the database
conn = sqlite3.connect('form_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SELECT query to retrieve data from the form_data table
cursor.execute('SELECT * FROM form_data')

# Fetch all records from the result set
records = cursor.fetchall()

# Print the fetched records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
conn.close()
