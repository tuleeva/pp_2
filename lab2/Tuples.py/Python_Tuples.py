#Tuples are used to store multiple items in a single variable.
#Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)