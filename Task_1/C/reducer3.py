#!/usr/bin/python
from itertools import groupby
from operator import itemgetter
import sys

def read(file):
    for line in file:
        print(line)

def main():
    data = read(sys.stdin)


main()
