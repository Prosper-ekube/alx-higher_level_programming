#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == "":
        return None
    elif my_list != "":
        biggestInt = my_list[0]
        for i in range(len(my_list)):
            if biggestInt < my_list[i]:
                biggestInt = my_list[i]

    return biggestInt
