import subprocess 
import os
from datetime import datetime

# Function to write command output to a file
def create_backup(source_directory):
    if not os.path.exists(source_directory):
        print(f"Error: The directory '{source_directory}' does not exist.")
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Task 1: Listing all running processes
def list_processes():
    try:
        # Run the system command to list processes (platform-specific)
        if subprocess.os.name == "nt":  # command used For Windows
            command = ["tasklist"]
        else:  # For Unix/Linux/Mac
            command = ["ps", "-aux"]

        # Execute the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        filename = f"process_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        write_to_file(filename, result.stdout)
        print(f"Process list saved to {filename}")
    except Exception as e:
        print(f"Error listing processes: {e}")

# Task 2: Monitoring system resource usage
def monitor_resources():
    try:
        # Run the system command to monitor resources (platform-specific)
        if subprocess.os.name == "nt":  # For Windows
            command = ["typeperf", "\\Processor(_Total)\\% Processor Time"]
        else:  # For Unix/Linux/Mac
            command = ["top", "-b", "-n", "1"]  # Top in batch mode for one iteration

        # Execute the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        filename = f"system_resources_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" # did not understand this especialy the strftime thing 
        write_to_file(filename, result.stdout)
        print(f"System resource usage  is saved to {filename}")
    except Exception as e:
        print(f"Error monitoring resources: {e}")

if __name__ == "__main__": # __ creats the object into an string 
    list_processes()
    monitor_resources()

