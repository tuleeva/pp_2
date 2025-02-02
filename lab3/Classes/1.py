#Define a class which has at least two methods:
# `getString`: to get a string from console input
# `printString`: to print the string in upper case.

# class MyClass:
#     def __init__(self):
#         self.input_string = ""

#     def getString(self):
#         # Get a string from console input
#         self.input_string = input("Enter a string: ")

#     def printString(self):
#         # Print the string in upper case
#         print(self.input_string.upper())
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()