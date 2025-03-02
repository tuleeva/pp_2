#write a python program to delete file by specified path.
import os
file_path = input("Enter the path to file: ")
if os.path.exists(file_path):
    if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"The file {file_path} does not exist.")
            except Exception as e:
                 print(f"An error: {e}")
    else:
        print(f"The file {file_path} is not file.")
else:
    print(f"The file {file_path} does not exist.")