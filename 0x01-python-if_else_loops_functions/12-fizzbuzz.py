#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz ", end="")
        elif numbers % 3 == 0:
            print("Fizz ", end="")
        elif numbers % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numbers), end="")
