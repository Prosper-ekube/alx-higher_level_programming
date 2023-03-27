#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    args = sys.argv[1:]

    if len(args) == 0:
        print(f"{len(args)} arguments.")
    else:
        num_args = len(args)
        if num_args == 1:
            print(f"{num_args} argument:")
        else:
            print(f"{num_args} arguments:")
        for i in args:
            arg_position = args.index(i)
            arg_value = args[arg_position]
            print(f"{arg_position + 1}: {arg_value}")
