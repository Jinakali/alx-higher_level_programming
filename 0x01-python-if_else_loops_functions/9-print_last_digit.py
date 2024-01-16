#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = -1
    number = number * sign
    print("{}".format(number % 10), end='')
    return number % 10
