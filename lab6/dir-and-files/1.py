#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
def Directories(path):
    try:
        directories = [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]
        return directories
    except FileNotFoundError:
        return "The specified path doesn't exist."

def Files(path):
    try:
        files = [entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))]
        return files
    except FileNotFoundError:
        return "The specified path doesn't exist."

def All(path):
    try:
        all_file_directories = os.listdir(path)
        return all_file_directories
    except FileNotFoundError:
        return "The specified path doesn't exist."

def main():
    path = input("Enter the path: ")
    # example:  C:\Users\User\Desktop\pp_2\labs\lab6

    print("Directories in the path: ")
    print(Directories(path))

    print("Files in the path: ")
    print(Files(path))

    print("All files and directories in the path: ")
    print(All(path))

if __name__ =="__main__":
    main()