import os
import json
import datetime

# Define the directories where data will be stored and logs will be saved
storage_dir = "F:/sandbox/PMP_Project"
log_dir = "F:/sandbox/PMP_Project/PMP_Study_Data/logs"

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Function to log actions (saves, loads, backups)
def log_action(action, agent_name, success=True, message=""):
    log_file = os.path.join(log_dir, f"{agent_name}_log.txt")
    with open(log_file, 'a') as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] Action: {action}, Success: {success}, Agent: {agent_name}, Details: {message}\n")

# Function to save data to a JSON file
def save_data(agent_name, user_data, backup=False):
    # Create a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Construct the file path where the data will be saved
    file_path = os.path.join(storage_dir, agent_name, f"{agent_name}_data_{timestamp}.json")
    
    # Ensure agent directory exists
    agent_dir = os.path.join(storage_dir, agent_name)
    if not os.path.exists(agent_dir):
        os.makedirs(agent_dir)

    # Add a creation time field to the user data
    user_data["creation_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save the data to a file
    with open(file_path, 'w') as file:
        json.dump(user_data, file)
        log_action("save", agent_name, message=f"Data saved locally at {file_path}")
    
    # Optionally, back up the file
    if backup:
        backup_dir = os.path.join(storage_dir, "backups")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        backup_file_path = os.path.join(backup_dir, f"{agent_name}_backup_{timestamp}.json")
        with open(backup_file_path, 'w') as backup_file:
            json.dump(user_data, backup_file)
            log_action("backup", agent_name, message=f"Data backed up to {backup_file_path}")

# Function to load data from a JSON file
def load_data(agent_name):
    # Get the most recent file by sorting files in the directory
    agent_dir = os.path.join(storage_dir, agent_name)
    all_files = [f for f in os.listdir(agent_dir) if f.endswith(".json")]
    if not all_files:
        log_action("load", agent_name, success=False, message="No data files found")
        return None
    latest_file = max(all_files, key=lambda f: os.path.getctime(os.path.join(agent_dir, f)))
    file_path = os.path.join(agent_dir, latest_file)

    # Load the data
    with open(file_path, 'r') as file:
        data = json.load(file)
        log_action("load", agent_name, message=f"Data loaded from {file_path}")
        return data
