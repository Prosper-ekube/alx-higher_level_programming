#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedDictionary = sorted(a_dictionary.keys())
    for i in sortedDictionary:
        print(f"{i}: {a_dictionary[i]}")
