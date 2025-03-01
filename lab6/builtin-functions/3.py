#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_Palindrome(string):
    string = string.replace(" ", "").lower() #убираем пробелы если они есть и переводим в маленькие буквы
    return string == string[::-1]

string = input("input a string: ")
if is_Palindrome(string):
    print("Yes, it's palindrome!")
else:
    print("No, it's not palindrome.")