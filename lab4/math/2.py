# 2. Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
import math
height=int(input("Height: "))
value1=int(input("Base, first value: "))
value2=int(input("Base, second value: "))
area=(value1+value2)*height/2
print(f"Area: {area}")