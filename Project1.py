#!/usr/bin/env python

import sys


def main():
    argfile = sys.argv[1]
    with open(argfile) as source:
        for line in source:
            numbers = map(int, line.split())
            find_max_sum(numbers)


def find_max_sum(numbers):
    max_sum = 0;
    max_i = -1
    max_j = -1
    i = 0
    j = len(numbers)
    while i < j:
        subarray_sum = 0
        for x in range(i, j):
            subarray_sum += numbers[x]
            if subarray_sum > max_sum:
                max_i = i
                max_j = x
                max_sum = subarray_sum
        i += 1
    max_sum_subarray = numbers[max_i:(max_j+1)]
    print numbers
    print max_sum_subarray
    print max_sum
    print ''


main()
