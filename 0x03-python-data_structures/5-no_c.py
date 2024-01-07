#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            new_str = my_string[:i] + my_string[i + 1:]
        else:
            new_str = my_string
    return new_str
