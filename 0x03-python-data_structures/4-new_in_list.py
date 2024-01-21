#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_limit = len(my_list)
    if idx < 0:
        my_list_cpy = my_list
        return my_list_cpy
    if idx >= len(my_list):
        my_list_cpy = my_list
        return my_list_cpy
    new_list = []
    for i in my_list:
        new_list.append(i)
    new_list[idx] = element
    return new_list
