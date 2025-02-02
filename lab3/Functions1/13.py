#Write a program able to play the `"Guess the number"` - game,
#  where the number to be guessed is randomly chosen between 1 and 20. 
import random
def Guess_The_Number():
    num=random.randint(1, 20)
    print("Hello! What is your name?\n")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    count_of_guesses = 0
    while True:
        guess_num=int(input("Take a guess.\n"))
        count_of_guesses += 1
        if guess_num < num:
            print("Your guess is too low.")
        elif guess_num > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count_of_guesses} guesses!")
            break

Guess_The_Number()