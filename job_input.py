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

@app.route('/recruiter.html')
def recruiter():
    return render_template('recruiter.html')

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
        facebook TEXT,
        experience TEXT,
        avg1 FLOAT,
        avg2 FLOAT,
        avg3 FLOAT,
        avg4 FLOAT,
        avg5 FLOAT
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
        facebook = data.get("facebook")
        experience = data.get("experience")
        avg1 = data.get("avg1")
        avg2 = data.get("avg2")
        avg3 = data.get("avg3")
        avg4 = data.get("avg4")
        avg5 = data.get("avg5")
        # avg6 = data.get("avg6")
        # avg7 = data.get("avg7")
        # avg8 = data.get("avg8")
        # avg9 = data.get("avg9")
        # avg10 = data.get("avg10")

        print(name, position, contact, linkedin, twitter,facebook,experience, avg1, avg2, avg3, avg4, avg5)

        cursor.execute('''
            INSERT INTO form_data (name, position, contact, linkedin, twitter,facebook, experience, avg1, avg2, avg3, avg4, avg5)
            VALUES (?, ?, ?, ?, ?,?,?, ?, ?, ?, ?, ?)
        ''', (name, position, contact, linkedin, twitter,facebook,experience, avg1, avg2, avg3, avg4, avg5))
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
    

@app.route('/getData')

def get_data():
    try:
        # Connect to the database
        conn = sqlite3.connect('form_data.db')
        cursor = conn.cursor()

        # Query the database to fetch name, position, experience, and contact number
        cursor.execute('SELECT name, position, experience, contact FROM form_data')
        data_from_db = cursor.fetchall()

        # Convert the query result to a list of dictionaries
        data_list = []
        for row in data_from_db:
            name, position, experience, contact = row
            data_dict = {
                'name': name,
                'department': position,
                'experience': experience,
                'contact': contact,
                'image_url': '../static/download.jpeg'
            }
            data_list.append(data_dict)

        # Close the database connection
        conn.close()

        # Return the data as JSON response
        return jsonify(data_list)
    except Exception as e:
        # Handle exceptions and send an error response to the frontend
        error_message = str(e)
        response_data = {"status": "error", "message": error_message}
        return jsonify(response_data), 500

@app.route('/<string:name>-<string:contact>')
def show_details(name, contact):
    try:
        # Connect to the database
        conn = sqlite3.connect('form_data.db')
        cursor = conn.cursor()

        # Query the database to fetch data for the specific name and contact number
        cursor.execute('SELECT name, position, contact, linkedin, twitter,facebook, experience, avg1, avg2, avg3, avg4, avg5 FROM form_data WHERE name = ? AND contact = ?', (name, contact))
        data_from_db = cursor.fetchone()

        # Close the database connection
        conn.close()

        # If data is found, return it as a JSON response
        if data_from_db:
            name, position, contact, linkedin, twitter, facebook, experience, avg1, avg2, avg3, avg4, avg5 = data_from_db
            data_dict = {
                'name': name,
                'position': position,
                'contact': contact,
                'linkedin': linkedin,
                'twitter': twitter,
                'facebook': facebook,
                'experience': experience,
                'avg1': avg1,
                'avg2': avg2,
                'avg3': avg3,
                'avg4': avg4,
                'avg5': avg5
            }
            return render_template('employee_details.html', data_dict=data_dict)
        else:
            # If no data is found, return a not found response
            response_data = {"status": "error", "message": "Data not found"}
            return jsonify(response_data), 404

    except Exception as e:
        # Handle exceptions and send an error response to the frontend
        error_message = str(e)
        response_data = {"status": "error", "message": error_message}
        return jsonify(response_data), 500



if __name__ == '__main__':
    app.run(debug=True)
