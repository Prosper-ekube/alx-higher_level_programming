#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    args = sys.argv[1:]

    if len(args) == 0:
        print(f"{len(args)} arguments.")
    else:
        arg_position = args.index(args[0])
        arg_value = args[arg_position]
        num_args = len(args)
        print(f"{num_args} argument:")
        print(f"{arg_position}: {arg_value}")
