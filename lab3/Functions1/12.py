#Define a function `histogram()` that takes a list of integers and prints a histogram to the screen.
# For example, `histogram([4, 9, 7])` should print the following:
#```
#****
#*********
#*******
#```

def histogram(lst):
    for num in lst:
        print('*' * num)
nums=input().split()
nums=[int(i) for i in nums] #строки в целые числа
histogram(nums)