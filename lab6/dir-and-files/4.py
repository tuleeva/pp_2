#Write a Python program to count the number of lines in a text file.
def count_lines(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file in '{path}' doesn't exist")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
def main():
    path = input("Enter the path: ")
    #input example: C:\Users\User\Desktop\pp_2\labs\lab6\dir-and-files\for_examples\text.txt
    Count = count_lines(path)
    if Count > 0:
        print(f"The file in '{path}' contains {Count} lines")
    
if __name__ == "__main__":
    main()