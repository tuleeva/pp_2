#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def check(tuples):
    return all(tuples)
my_tuple = (1, 2, 3, 4)
result = check(my_tuple)
print(result)

my_tuple = (1, 0, 3, 4)
result = check(my_tuple)
print(result)