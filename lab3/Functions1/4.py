#You are given list of numbers separated by spaces.
#  Write a function `filter_prime` which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
primes = filter_prime(numbers)
print(f"Prime numbers: {primes}")