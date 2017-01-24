#!/usr/bin/env python

import sys


def main():
    arg_file = sys.argv[1]
    process_file_for_enumeration(arg_file)
    process_file_for_better_enumeration(arg_file)


# Algorithm 1
def process_file_for_enumeration(arg_file):
    with open(arg_file) as source:
        for line in source:
            numbers = map(int, line.split())
            find_max_sum_enumeration(numbers)


def find_max_sum_enumeration(numbers):
    max_sum = 0
    max_i = -1
    max_j = -1
    i = 0
    j = len(numbers)
    while i < j:
        k = i
        # starting with each index, we want to calculate
        # the sum of each sub array ending in the
        # remaining indexes
        while k < j+1:
            m = i
            sub_array_sum = 0
            # calculate sum of sub array
            while m < k:
                sub_array_sum += numbers[m]
                m += 1
            if sub_array_sum > max_sum:
                max_i = i
                max_j = m
                max_sum = sub_array_sum
            k += 1
        i += 1

    max_sum_sub_array = numbers[max_i:max_j]

    # TODO Change this to export to file instead of simply printing
    print numbers
    print max_sum_sub_array
    print max_sum
    print ''


# Algorithm 2
def process_file_for_better_enumeration(arg_file):
    with open(arg_file) as source:
        for line in source:
            numbers = map(int, line.split())
            find_max_sum_better_enumeration(numbers)


def find_max_sum_better_enumeration(numbers):
    max_sum = 0
    max_i = -1
    max_j = -1
    i = 0
    j = len(numbers)
    while i < j:
        sub_array_sum = 0
        # calculate the sum of the sub array for this index
        # to another index. Keep the running total and keep
        # adding on so we don't have to recalculate them
        for x in range(i, j):
            sub_array_sum += numbers[x]
            if sub_array_sum > max_sum:
                max_i = i
                max_j = x
                max_sum = sub_array_sum
        i += 1

    max_sum_sub_array = numbers[max_i:(max_j+1)]

    # TODO Change this to export to file instead of simply printing
    print numbers
    print max_sum_sub_array
    print max_sum
    print ''


main()
