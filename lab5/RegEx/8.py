#Write a Python program to split a string at uppercase letters.
import re
def split_at_uppercase(s):
    return re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=\s|$)', s)
test = "ThisIsString"
result = split_at_uppercase(test)
print(f"Split String: {result}")