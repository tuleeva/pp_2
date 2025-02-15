# 3. Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
import math
side=int(input("Input number of sides: "))
length=int(input("Input the length of a side: "))
area=((length**2)*side)/(4*(math.tan(math.pi/side)))
print(int(area))