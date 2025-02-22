#Implement a generator that returns all numbers from (n) down to 0.
def down(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
result= down(n)

for el in result:
    print(el)