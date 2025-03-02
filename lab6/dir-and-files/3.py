#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
def Check(path):
    if os.path.exists(path):
        print(f"The path '{path}' is exists")

        directory_name = os.path.dirname(path)
        file_name = os.path.basename(path)

        print(f"Directory name: {directory_name}")
        print(f"File name: {file_name}")

    else:
        print(f"The path '{path}' doesn't exists")

def main():
    path = input("Enter the path: ")

    Check(path)

if __name__ == "__main__":
    main()