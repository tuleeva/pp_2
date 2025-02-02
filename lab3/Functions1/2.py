#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
#  The following formula is used for the conversion:
#`C = (5 / 9) * (F – 32)`
def my_func(F):
    C = (5 / 9) * (F - 32)
    print(C)
my_func(int(input()))