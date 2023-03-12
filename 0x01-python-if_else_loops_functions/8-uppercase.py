#!/usr/bin/python3

def to_upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    string_new = ""
    for char in str:
        string_new += "%c" % to_upper(char)
    print("{:S}".format(string_new))
