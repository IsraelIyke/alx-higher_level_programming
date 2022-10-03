#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        length = len(sentence)
        return length, None
    else:
        str1 = sentence
        str2 = len(str1)
        str1.split()
        return str2, str1[0]
