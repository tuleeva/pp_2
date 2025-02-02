#Write a function that accepts string from user and print all permutations of that string.
import itertools
def Permutations():
    word=input()
    permutations = itertools.permutations(word)
    for perm in permutations:
        print(''.join(perm))

Permutations()