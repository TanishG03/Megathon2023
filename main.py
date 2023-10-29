import subprocess

# https://www.linkedin.com/in/ponguru/
# https://twitter.com/ponguru
# https://www.facebook.com/ponnurangam.kumaraguru
# https://www.linkedin.com/in/dhattarwalaman/
# https://twitter.com/AmanDhattarwal
# https://www.facebook.com/dhattarwalaman
import sqlite3
import pandas as pd
import joblib
# Connect to the database
name=input("Enter Name:")
contact=input("Enter Contact Number:")
conn = sqlite3.connect('form_data.db')
cursor = conn.cursor()

cursor.execute('SELECT name, position, contact, linkedin, twitter,facebook, experience, avg1, avg2, avg3, avg4, avg5 FROM form_data WHERE name = ? AND contact = ?', (name, contact))
data_from_db = cursor.fetchone()
conn.close()


name, position, contact, linkedin, twitter, facebook, experience, avg1, avg2, avg3, avg4, avg5 = data_from_db
print(linkedin)
print(twitter)
print(facebook)
linkedIn_url = linkedin
twitter_url = twitter
fb_url = facebook
# List of Python scripts to be executed
script_paths = [
    #  "COMBINED/LinkedIn/LinkedIn_scrapper.py", linkedIn_url,
    #  "COMBINED/LinkedIn/LinkedIn_processor_basic.py",
    #  "COMBINED/LinkedIn/LinkedIn_processor_activities.py",
    #  "COMBINED/LinkedIn/LinkedIn_processor_education.py",
    #  "COMBINED/LinkedIn/LinkedIn_processor_experince.py",
    #  "COMBINED/LinkedIn/LinkedIn_processor_skills.py",
    #  # "COMBINED/LinkedIn/LinkedIn_processor_courses.py",
    #  # "COMBINED/LinkedIn/LinkedIn_processor_honors.py",
    #  # "COMBINED/LinkedIn/LinkedIn_processor_projects.py",
    #  # "COMBINED/LinkedIn/LinkedIn_processor_testscores.py",
    # "COMBINED/Twitter/Twitter_scrapper.py", twitter_url,
    # "COMBINED/Twitter/Twitter_processor.py",
    # "COMBINED/Facebook/Facebook_scrapper.py", fb_url,
    # "COMBINED/Facebook/Facebook_processor.py",
    "COMBINED/Analysis/analysis.py",
    "COMBINED/scraed_data_ln.txt",
    "COMBINED/scraed_data_tw.txt",
    "COMBINED/scraed_data_fb.txt",
]

# Function to run the Python scripts
def run_scripts(script_paths):
    for i in range(0, len(script_paths) - 3):
        if script_paths[i] == linkedIn_url or script_paths[i] == twitter_url or script_paths[i] == fb_url:
            continue
        try:
            # Run the Python script using subprocess
            subprocess.run(["python3", script_paths[i], script_paths[i+1], script_paths[i+2], script_paths[i+3]], check=True)
            print(f"Script '{script_paths[i]}' executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing '{script_paths[i]}': {e}")

# Run the scripts
run_scripts(script_paths)
# Load your new data point(s) into a pandas DataFrame

import csv

with open('wow.txt', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None)
    data = []
    for item in reader:
        data.append(item)
openness = float(data[0][0])
conscientiousness = float(data[0][1])
extraversion = float(data[0][2])
agreeableness = float(data[0][3])
emotional_stability = float(data[0][4])

# Create a DataFrame for the user input
new_data = pd.DataFrame({
    'Openness': [openness],
    'Conscientiousness': [conscientiousness],
    'Extraversion': [extraversion],
    'Agreeableness': [agreeableness],
    'Emotional Stability': [emotional_stability]
})

# Load the saved model and label encoders
classifier, label_encoders = joblib.load('ML_ocean_1.pkl')

# Predict numerical values for the new data point(s)
predicted_values = classifier.predict(new_data)

# Convert the predicted numerical values back to string labels
predicted_labels = []
for i, le in enumerate(label_encoders):
    predicted_labels.append(le.inverse_transform(predicted_values[:, i]))

# Print the predicted string values
for label in predicted_labels:
    print(label[0])


model2=joblib.load('ML_ocean.pkl')
feature_names = ['c','n','a','e','o']
feature_values = [0,0,0,0,0]
feature_values[0]=conscientiousness
feature_values[1]=5-emotional_stability
feature_values[2]=agreeableness
feature_values[3]=extraversion
feature_values[4]=openness
values=pd.DataFrame([feature_values], columns=feature_names)
predicted_label = model2.predict(values)
print("This person is suitable to the roles: ", predicted_label[0])
print("Political: ", data[0][5])
print("Tech: ", data[0][6])
print("Sales: ", data[0][7])
