#!/usr/bin/python3
import sys
with open(sys.argv[1], "r") as file:
    with open(sys.argv[2], "w") as ret:
        read = file.read()
        ret.write(read)
