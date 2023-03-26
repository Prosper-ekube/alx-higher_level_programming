def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        maxxx = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > maxxx:
                maxxx = my_list[i]
        return maxxx
