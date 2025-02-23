#Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type,and can even change type after they have been set.
z = 4       # z is of type int
w = "Sally" # z is now of type str
print(z)

#If you want to specify the data type of a variable, this can be done with casting.
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0

#You can get the data type of a variable with the type() function.
d = 5
e = "John"
print(type(d))
print(type(e))

#String variables can be declared either by using single or double quotes:
q = "John"
# is the same as
q = 'John'

#Variable names are case-sensitive.This will create two variables:
p = 4
P = "Sally"
#P will not overwrite p