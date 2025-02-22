#Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(camel):
    snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel).lower()
    return snake
test = "thisIsString"
print(f"Camel Case: {test}")
result = camel_to_snake(test)
print(f"Snake Case: {result}")