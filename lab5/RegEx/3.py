# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
tests = ["Hello", "he_llo", "hello_world", "HELL_o", "_hello"]
for test in tests:
    x = re.search("^[a-z]+(_[a-z]+)*$", test)
    if x:
        print(f"Yes, we have match for: {test}")
    else:
        print(f"No match for: {test}")