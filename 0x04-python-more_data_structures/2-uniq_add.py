#!/usr/bin/python3
'''
create a set from the list
add up elements in set
'''


def uniq_add(my_list=[]):
    if my_list is None:
        return None
    new = set(my_list)
    result = 0
    for i in new:
        result += i
    return result
