from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Define a route to render the form page
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/employee.html')
def employee():
    return render_template('employee.html')

# Connect to SQLite database
conn = sqlite3.connect('form_data.db')
cursor = conn.cursor()

# Create a table to store form data if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS form_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        contact TEXT,
        linkedin TEXT,
        twitter TEXT,
        question1 INTEGER,
        question2 INTEGER,
        question3 INTEGER,
        question4 INTEGER,
        question5 INTEGER,
        question6 INTEGER,
        question7 INTEGER,
        question8 INTEGER,
        question9 INTEGER,
        question10 INTEGER
    )
''')
conn.commit()

# Close the connection after creating the table
conn.close()

@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        # Get form data from the request
        data = request.get_json()

        # Extract form fields
        name = data.get("name")
        contact = data.get("contact")

        # Check if record with the same name and contact number exists
        conn = sqlite3.connect('form_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM form_data WHERE name = ? AND contact = ?', (name, contact))
        existing_record = cursor.fetchone()

        if existing_record:
            # Record with the same name and contact number already exists
            conn.close()
            response_data = {"status": "error", "message": "Record already exists"}
            return jsonify(response_data), 400

        # If record does not exist, insert into the database
        position = data.get("position")
        linkedin = data.get("linkedin")
        twitter = data.get("twitter")
        question1 = data.get("question1")
        question2 = data.get("question2")
        question3 = data.get("question3")
        question4 = data.get("question4")
        question5 = data.get("question5")
        question6 = data.get("question6")
        question7 = data.get("question7")
        question8 = data.get("question8")
        question9 = data.get("question9")
        question10 = data.get("question10")

        print(name, position, contact, linkedin, twitter, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)

        cursor.execute('''
            INSERT INTO form_data (name, position, contact, linkedin, twitter, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, position, contact, linkedin, twitter, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10))
        conn.commit()
        conn.close()

        # Send a success response to the frontend
        response_data = {"status": "success", "message": "Form submitted successfully!"}
        return jsonify(response_data), 200
    except Exception as e:
        # Handle exceptions and send an error response to the frontend
        error_message = str(e)
        response_data = {"status": "error", "message": error_message}
        return jsonify(response_data), 500

if __name__ == '__main__':
    app.run(debug=True)
