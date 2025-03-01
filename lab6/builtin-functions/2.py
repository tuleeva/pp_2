#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def Count(string):
    upper_count=0
    lower_count=0
    for char in string:
        if char.isupper():
            upper_count+=1
        if char.islower():
            lower_count+=1
    return upper_count, lower_count

string = input("Input a string: ")
upper, lower = Count(string)
print(f"number of upper case letters: {upper}")
print(f"number of lower case letters: {lower}")