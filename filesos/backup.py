import os
import shutil
import datetime

directory_path = input("Enter the directory path to back up")
if not os.path.isdir("directory_path"):
    print("the directory path that you have given does not exist")
    exit()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"backup_{timestamp}"

backup_path = shutil.make_archive(backup_name, 'zip', directory_path)

print(f"Backup successfully created at: {backup_path}")



## dont forget to push the code after youre done 




























"""
import os
import shutil
from datetime import datetime

# Step 1: Get user input for directory path
directory_path = input("Enter the directory path to back up: ")

# Step 2: Validate the directory
if not os.path.exists(directory_path):
    print("The provided directory path does not exist. Please try again.")
    exit()

# Step 3: Create a timestamped backup name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_name = f"backup_{timestamp}"

# Step 4: Create the zip archive
backup_path = shutil.make_archive(backup_name, 'zip', directory_path)

# Step 5: Confirm backup creation
print(f"Backup successfully created at: {backup_path}")


"""