#1.create new file and write something and put into specific folder

import os

# Define the folder path
folder_path = 'fileOperation'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the file path including the folder
file_path = os.path.join(folder_path, 'newfileOps1.txt')

# Write data to the file inside the specified folder
with open(file_path, 'w') as file:
    file.write("hello, this is a new file")
