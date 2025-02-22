#Write a Python program to insert spaces between words starting with capital letters.
import re
def spaces(s):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2' , s)
test = "ThisIsString"
result = spaces(test)
print(f"String with spaces: {result}")