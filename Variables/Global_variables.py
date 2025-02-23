#Create a variable outside of a function, and use it inside the function:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y)

#To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)

#To change the value of a global variable inside a function,
#refer to the variable by using the global keyword:

b = "awesome"

def myfunc():
  global b
  b = "fantastic"

myfunc()

print("Python is " + b)