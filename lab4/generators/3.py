#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible(n):
    for el in range(0, n+1):
            if el%3==0 and el%4==0:
                  yield el
n=int(input())   
result=divisible(n)
print(",".join(map(str, result)))