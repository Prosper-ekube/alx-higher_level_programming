#!/usr/bin/python3

for i in range(122, 64, -1):
    print("{:c}".format(i).upper() if i % 2 == 0
          else "{:c}".format(i).lower(), end="")
