#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
tests = "Hi, this is a test. sentence."
x = re.sub(r"[ ,.]", ":", tests)
print(x)