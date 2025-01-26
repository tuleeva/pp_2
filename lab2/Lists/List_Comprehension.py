#List Comprehension
#List comprehension offers a shorter syntax when you 
# want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Condition
#The condition is like a filter that only accepts the items that evaluate to True.
newlist = [x for x in fruits if x != "apple"]

#The condition is optional and can be omitted:
newlist = [x for x in fruits]

#Iterable
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

#Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]

#The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list:
#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

#The expression in the example below says:
#"Return the item if it is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]