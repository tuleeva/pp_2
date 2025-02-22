#Write a Python program to drop microseconds from datetime.
import datetime

x=(datetime.datetime.now())
result=x.replace(microsecond=0)
print(f"Current date: {x}")
print(f"Date without microseconds:{result}")