#Write a Python program to copy the contents of a file to another file
import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"File copied successfully from {src} to {dest}")
    except Exception as e:
        print(f"An error {e}")

def main():
    src = input("Enter the path of the source file: ")
    dest = input("Enter the path of the destination file: ")
    #inputs: 
    # src: C:\Users\User\Desktop\pp_2\labs\lab6\dir-and-files\for_examples\A.txt
    # dest: C:\Users\User\Desktop\pp_2\labs\lab6\dir-and-files\for_examples\text.txt
    copy_file(src, dest)

if __name__ == "__main__":
    main()