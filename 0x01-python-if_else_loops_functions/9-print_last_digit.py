#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(numbers):
    """Print the last digit of a number and return it."""
    print(abs(numbers) % 10, end="")
    return (abs(numbers) % 10)

