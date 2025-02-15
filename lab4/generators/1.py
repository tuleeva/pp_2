#Create a generator that generates the squares of numbers up to some number N.
import math
def squares(N):
    for i in range(N+1):
        yield pow(i, 2)

N=int(input())
result = squares(N)

for el in result:
    print(el)    
