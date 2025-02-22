#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
tests =  ["anb", "adeab", "adobb", "asb", "aDba"]
for test in tests:
   x = re.search("^a.*b$", test)
   if x:
     print(f"YES! We have a match for: {test}")
   else:
     print(f"No match for: {test}")