#!/usr/bin/python3

if __name__ == "__main__":

    import calculator_1

    import sys

    args = sys.argv[1:]

    num_args = len(args)

    plus = "+"
    minus = "-"
    times = "*"
    divide = "/"

    operators = [plus, minus, times, divide]

    Add = calculator_1.add
    Sub = calculator_1.sub
    Mul = calculator_1.mul
    Div = calculator_1.div

    if num_args != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif args[1] not in args:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif args[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        x = int(args[0])
        y = int(args[2])

        if plus in args:
            print("{} + {} = {}".format(x, y, Add(x, y)))
            sys.exit(0)
        if minus in args:
            print("{} - {} = {}".format(x, y, Sub(x, y)))
            sys.exit(0)
        if times in args:
            print("{} * {} = {}".format(x, y, Mul(x, y)))
            sys.exit(0)
        if divide in args:
            print("{} / {} = {}".format(x, y, Div(x, y)))
            sys.exit(0)
