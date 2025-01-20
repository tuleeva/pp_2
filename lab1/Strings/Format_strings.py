#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age  #IT'S WRONG
print(txt)

#But we can combine strings and numbers by using f-strings or the format() method!

#F-Strings
#To specify a string as an f-string, simply put an f in front of the string literal,
#  and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)


#Placeholders and Modifiers
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
