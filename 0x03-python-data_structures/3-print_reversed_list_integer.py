#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index_limit = len(my_list) - 1
    for i in range(index_limit, -1, -1):
        print("{:d}".format(my_list[i]))