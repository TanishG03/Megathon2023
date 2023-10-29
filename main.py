import subprocess

# https://www.linkedin.com/in/ponguru/
# https://twitter.com/ponguru
# https://www.facebook.com/ponnurangam.kumaraguru
# https://www.linkedin.com/in/dhattarwalaman/
# https://twitter.com/AmanDhattarwal
# https://www.facebook.com/dhattarwalaman
import sqlite3
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
     "COMBINED/LinkedIn/LinkedIn_scrapper.py", linkedIn_url,
     "COMBINED/LinkedIn/LinkedIn_processor_basic.py",
     "COMBINED/LinkedIn/LinkedIn_processor_activities.py",
     "COMBINED/LinkedIn/LinkedIn_processor_education.py",
     "COMBINED/LinkedIn/LinkedIn_processor_experince.py",
     "COMBINED/LinkedIn/LinkedIn_processor_skills.py",
     # "COMBINED/LinkedIn/LinkedIn_processor_courses.py",
     # "COMBINED/LinkedIn/LinkedIn_processor_honors.py",
     # "COMBINED/LinkedIn/LinkedIn_processor_projects.py",
     # "COMBINED/LinkedIn/LinkedIn_processor_testscores.py",
    "COMBINED/Twitter/Twitter_scrapper.py", twitter_url,
    "COMBINED/Twitter/Twitter_processor.py",
    "COMBINED/Facebook/Facebook_scrapper.py", fb_url,
    "COMBINED/Facebook/Facebook_processor.py",
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
