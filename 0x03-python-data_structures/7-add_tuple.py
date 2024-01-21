#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = []
    list_b = []
    if len(tuple_a) >= 2:
        for i in range(2):
            list_a.append(tuple_a[i])
    elif len(tuple_a) == 1:
        list_a = [tuple_a[0], 0]
    elif len(tuple_a) == 0:
        list_a = [0, 0]

    if len(tuple_b) >= 2:
        for i in range(2):
            list_b.append(tuple_b[i])
    elif len(tuple_b) == 1:
        list_b = [tuple_b[0], 0]
    elif len(tuple_b) == 0:
        list_b = [0, 0]

    sum_tuple = list_a[0] + list_b[0], list_a[1] + list_b[1]
    return sum_tuple
