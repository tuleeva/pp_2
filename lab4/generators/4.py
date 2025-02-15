#Implement a generator called squares to yield the square of all numbers from (a) to (b).
#  Test it with a "for" loop and print each of the yielded values.
import math
def square(a,b):
    for i in range(a, b+1):
        yield pow(i, 2)

a=int(input())
b=int(input())

result = square(a,b)

for el in result:
    print(el)    
