#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    str_cpy = str
    str_cpy = str_cpy[:n] + str_cpy[n + 1:]
    return str_cpy