#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = str
    str_cpy = str_cpy[:n] + str_cpy[n + 1:]
    return str_cpy
