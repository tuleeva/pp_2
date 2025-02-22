#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
tests = ["ab", "aab", "abb", "abbb",  "b", "ba"]
for test in tests:
   x = re.search("^ab{2,3}$", test)
   if x:
    print(f"YES! We have a match for: {test}")
   else:
    print(f"No match for: {test}")