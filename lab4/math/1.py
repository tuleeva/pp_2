# 1. Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904
import math
degree=int(input("Input degree: "))
x=math.pi
radian=float((degree*x)/180)
result=f"{radian: .6f}"
print(result)