import subprocess

# https://www.linkedin.com/in/ponguru/
# https://twitter.com/ponguru
linkedIn_url = input("Enter LinkedIn URL: ")
twitter_url = input("Enter Twitter URL: ")

# List of Python scripts to be executed
script_paths = [
    # "LinkedIn/LinkedIn_scrapper.py", linkedIn_url,
    # "LinkedIn/LinkedIn_processor_basic.py",
    # "LinkedIn/LinkedIn_processor_activities.py",
    # "LinkedIn/LinkedIn_processor_education.py",
    # "LinkedIn/LinkedIn_processor_experince.py",
    # "LinkedIn/LinkedIn_processor_skills.py",
    # "LinkedIn/LinkedIn_processor_courses.py",
    # "LinkedIn/LinkedIn_processor_honors.py",
    # "LinkedIn/LinkedIn_processor_project.py",
    # "LinkedIn/LinkedIn_processor_testscores.py",
    "Twitter/Twitter_scrapper.py", twitter_url,
    "Twitter/Twitter_processor.py",
    "Analysis/analysis.py",
    "scraed_data_ln.txt",
    "scraed_data_tw.txt",
]

# Function to run the Python scripts
def run_scripts(script_paths):
    for i in range(0, len(script_paths) - 2):
        if script_paths[i] == linkedIn_url or script_paths[i] == twitter_url:
            continue
        try:
            # Run the Python script using subprocess
            subprocess.run(["python3", script_paths[i], script_paths[i+1], script_paths[i+2]], check=True)
            print(f"Script '{script_paths[i]}' executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing '{script_paths[i]}': {e}")

# Run the scripts
run_scripts(script_paths)
