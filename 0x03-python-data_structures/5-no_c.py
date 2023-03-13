#!/usr/bin/python3

def no_c(my_string):
    modString = my_string.translate({ord('c'): None})
    modString = modString.translate({ord('C'): None})
    return modString
