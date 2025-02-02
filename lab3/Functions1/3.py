# Write a program to solve a classic puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# `create function: solve(numheads, numlegs):`
def solve(numheads, numlegs):
    # x-number of chickens, y-number of rabbits
    # x + y = numheads
    # 2x + 4y = numlegs
    # x = numheads - y
    # 2(numheads - y) + 4y = numlegs
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    
    return x, y

numheads = int(input())
numlegs = int(input())
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")