import subprocess

# List of Python scripts to be executed
script_paths = [
    "LinkedIn_processor_basic.py",
    "LinkedIn_processor_activities.py",
    "LinkedIn_processor_courses.py",
    "LinkedIn_processor_education.py",
    "LinkedIn_processor_experince.py",
    "LinkedIn_processor_honors.py",
    "LinkedIn_processor_skills.py",
    "LinkedIn_processor_testscores.py"
]

# Function to run the Python scripts
def run_scripts(script_paths):
    for script_path in script_paths:
        try:
            # Run the Python script using subprocess
            subprocess.run(["python3", script_path], check=True)
            print(f"Script '{script_path}' executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing '{script_path}': {e}")

# Run the scripts
run_scripts(script_paths)
