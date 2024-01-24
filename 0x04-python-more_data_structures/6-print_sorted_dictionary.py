#!/usr/bin/python3
'''
sort list of dictionary key
print each key pair
'''


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    keys_sorted = sorted(a_dictionary)
    for i in keys_sorted:
        print("{}: {}".format(i, a_dictionary[i]))
