#Write a python program to convert snake case string to camel case string.
def snake_to_camel(snake):
    components = snake.split('_')
    return components[0] + ''.join(word.title() for word in components[1:])

test = "this_is_a_string"
print(f"Snake Case: {test}")
result = snake_to_camel(test)
print(f"Camel Case: {result}")