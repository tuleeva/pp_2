#Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path
import os

def check_for_access(path):

    if os.path.exists(path): #check if thr path exists
        print(f"The path '{path}' exists")

        if os.path.isfile(path): #check if the path is a file or directory
            print(f"The path '{path}' is a file")
        elif os.path.isdir(path):
            print(f"The path '{path}' is a directory")

        if os.access(path, os.R_OK):  #check if thr path is readable
            print(f"The path '{path}' is readable")
        else:
            print(f"The path '{path}' is not readable")

        if os.access(path, os.W_OK): #check if thr path is writable
            print(f"The path '{path}' is writeable")
        else:
            print(f"The path '{path}' is not writeable")

        if os.access(path, os.X_OK): #check if thr path is executable
            print(f"The path '{path}' is executable")
        else:
            print(f"The path '{path}' is not executable")
    
    else:
        print(f"The path '{path}' doesn't exist.")
def main():
    path = input("Enter the path: ")
    # example:  C:\Users\User\Desktop\pp_2\labs\lab6
    check_for_access(path)

if __name__ =="__main__":
    main()