import os
import datetime
import shutil 
"""
# Scan the example_directory and its subdirectories
for root, dirs, files in os.walk("./example_directory"):
    for file in files:
        file_path = os.path.join(root, file)
        # Check if the file is older than 1 minute
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if datetime.datetime.now() - file_mtime > datetime.timedelta(minutes=1):
            try:
                # Ask for confirmation to delete the file
                user_input = input(f"Do you want to delete {file_path}? (y/n): ").strip().lower()
                if user_input == "y":
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                else:
                    print(f"Skipped {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")

"""


def file_cleanup_bot(directory, days_old):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist")
        return 

    # calculate the cutoff time
    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(days=days_old)

    # create an 'Archive directory 
    archive_dir = os.path.join(directory, "Archive")
    os.makedirs(archive_dir, exist_ok = True)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        # Skip directories 
        if os.path.isdir(file_path):
            continue 

        # check file's modification time 
        file_mtime = datetime.datetime.fromtimestamp(os.path.gettime(file_path))
        if file_mtime < cutoff_time:
            shutil.move(file_path, os.path.join(archive_dir, file_name))
            print(f"Moved '{file_name}' to Archive")

    # Ask user for confirmation before detaling the archive folder 
    confirm = input (f"Do you want to delete the 'Archive' folder")
    if confirm == "yes":
        shutil.rmtree(archive_dir)
        print("Archive folder deleted.")

# example usuage 
file_cleanup_bot("./example_directory", 1)