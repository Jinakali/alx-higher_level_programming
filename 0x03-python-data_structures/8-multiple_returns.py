#!/usr/bin/python3
def multiple_returns(sentence):
    sent_length = len(sentence)
    return_list = []
    if sent_length > 0:
        return_list = [sent_length, sentence[0]]
    else:
        return_list = [sent_length, None]
    return_tuple = return_list[0], return_list[1]
    return return_tuple
