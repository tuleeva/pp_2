# #Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858
import math
import time
num = int(input("Enter a number: "))
delay = int(input("Enter a delay in milliseconds: "))
time.sleep(delay/1000)
result = math.sqrt(num)
print(f"Square root of {num} after {delay} milliseconds is {result}")