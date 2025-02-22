#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(n):
    for even in range(0, n+1, 2):
            yield even
n=int(input())   
even_nums=even(n)
print(",".join(map(str, even_nums)))