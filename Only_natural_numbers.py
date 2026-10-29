"""Program to calculate the square root of a number."""

def square_root(number):
    """Only natural numbers."""
    guess = 1

    while guess * guess != number:
        guess += 1

    return guess