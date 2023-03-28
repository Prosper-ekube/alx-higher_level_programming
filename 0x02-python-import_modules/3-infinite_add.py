#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    args = sys.argv[1:]
    summm = 0

    for i in args:
        arg_position = args.index(i)
        arg_value = args[arg_position]
        x = int(arg_value)
        summm += x

    print(summm)
