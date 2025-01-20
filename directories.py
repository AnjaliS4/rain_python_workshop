import os 
import shutil 
#ls -- k k cha
#cd -- change file 
#pwd - present working directory 

# create a new directory 
if not os.path.isdir("test_directory"):
    os.mkdir("test_directory")

# change the current working directory to the new directory 
os.chdir("test_directory") # if the path diesnt exist make it
print("Current working directory:", os.getcwd())

# create a text file in directory 
with open("example.txt", "w") as file:
    file.write("This is a test file")

# list files in the current directory 
print("files in directory:", os.listdir())

# copy the file 
shutil.copy("example.txt", "copy_example.txt")

# Move the copied file to a new location (renaming it in the process)

shutil.move("copy_example.txt", "../moved_example.txt") # .. means the the file should move one step ahead

# go back to the parent directory 
os.chdir("..")

# Remove the test directory and its contents 
shutil.rmtree("test_directory")
os.remove("moved_example.txt") # Remove the moved file 
print("Cleanup complete")