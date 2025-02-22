#Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
#Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Note: The values True and 1 are considered the same value in sets,
#  and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Note: The values False and 0 are considered the same value in sets,
#  and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)