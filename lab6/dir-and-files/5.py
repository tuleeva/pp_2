#Write a Python program to write a list to a file.
def list_into_file(path, my_list):
        try:
            with open(path, 'a') as file:
                for item in my_list:
                     file.write(str(item) + '\n')
            print("The list has been written")
        except Exception as e:
             print(f"An error: {e}")

def main():
    my_list = ['1', '2', '3', '4', '5']
    path = input("Enter the file path: ")
    #input example: C:\Users\User\Desktop\pp_2\labs\lab6\dir-and-files\for_examples\text.txt
    list_into_file(path, my_list)

if __name__ == "__main__":
     main()