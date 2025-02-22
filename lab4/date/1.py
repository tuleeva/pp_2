#Write a Python program to subtract five days from current date.
import datetime
x=datetime.datetime.now()
current=int(x.strftime("%d"))
print(current - 5)