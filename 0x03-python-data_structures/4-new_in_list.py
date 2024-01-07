#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_limit = len(my_list)
    if idx < 0:
        my_list_cpy = my_list
        return my_list_cpy
    if idx >= my_list_limit:
        my_list_cpy = my_list
        return my_list_cpy
    new_list = []
    for i in range(my_list_limit):
        new_list[i] = my_list[i]
    new_list[idx] = element
