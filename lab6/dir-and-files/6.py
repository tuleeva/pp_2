#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os
import string

def generate_files(directory_path):
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(f"hello! This is a file {file_name}")

def main():
    directory_path = input("Enter the path that already exists where you want to files be created: ")
    generate_files(directory_path)
    # example input: C:\Users\User\Desktop\pp_2\labs\lab6\dir-and-files\for_examples

if __name__ == "__main__":
    main()