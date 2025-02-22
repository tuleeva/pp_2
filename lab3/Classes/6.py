# Write a program which can filter prime numbers in a list by using `filter` function.
# Note: Use `lambda` to define anonymous functions.
is_prime = lambda n: n>1 and all(n%i != 0 for i in range(2, int(n**0.5) +1))
numbers = [10, 15, 3, 7, 13, 22, 23, 17, 18, 19]
prime_num = list(filter(is_prime, numbers))
print(prime_num)