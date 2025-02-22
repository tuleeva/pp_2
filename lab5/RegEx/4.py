#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
tests = ["Hello", "he_llo", "helloWorld", "HELLo", "Hell"]
for test in tests:
    x = re.search("^[A-Z][a-z]+$", test)
    if x:
        print(f"Yes, we have match for: {test}")
    else:
        print(f"No match for: {test}")