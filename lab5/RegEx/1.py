#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
tests =  ["ab", "aab", "abb", "b", "ba"]
for test in tests:
    x = re.search("^ab*$", test)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")