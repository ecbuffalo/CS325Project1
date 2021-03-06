#!/usr/bin/env python

import sys
import os.path
import random


def main():
    if len(sys.argv) == 2:
        first_arg = sys.argv[1]
        if os.path.isfile(first_arg):
            process_input_file(first_arg)
        else:
            try:
                test_num = int(first_arg)
                process_test_run(test_num)
            except ValueError:
                print "File does not exist or not valid integer to test with"
    else:
        print "Incorrect number of arguments. Only pass in 1 argument"


def process_test_run(test_run_number):
    i = 0
    test_array = []
    while i < test_run_number:
        val = random.randint(-100,100)
        test_array.append(val)
        i += 1

    print "Finding max sum using Algorithm 1"
    find_max_sum_enumeration(test_array)

    print "Finding max sum using Algorithm 2"
    find_max_sum_better_enumeration(test_array)


def process_input_file(arg_file):
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

# Algorithm 3
def find_max_cross(numbers, low, mid, high):
    """
    Find the max sub-array that crosses the midpoint of an array. Code is based
    off the pseudocode in the textbook 'Introduction to Algorithms Third Edition'
    by Thomas Cormen, Charles Leiserson, Ronald Rivest, and Clifford Stein. It is
    located on page 71.

    numbers: The input list to comput the max crossing sub array for.
    low: The starting index
    mid: The middle index of numbers
    high: The last index of numbers
    """
    left_sum = float('-inf')
    temp_sum = 0
    max_left = mid
    max_right = mid + 1
    for i in range(mid, low, -1):
        temp_sum += numbers[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i
    right_sum = ('-inf')
    temp_sum = 0
    for j in range(mid + 1, high + 1):
        sum += numbers[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def divide_and_conquer(numbers, low, high):
    """
    Find the max sub-array of an array including its indices and value. Code is based
    off the pseudocode in the textbook 'Introduction to Algorithms Third Edition' by Thomas Cormen, Charles Leiserson,
    Ronald Rivest, and Clifford Stein. It is located on page 72.


    numbers: The input list to compute the maximum subarray for.
    low: The starting index of numbers
    high: The ending index of numbers
    """
    if low == high:
        return low, high, numbers[low]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = divide_and_conquer(numbers, low, mid)
        right_low, right_high, right_sum = divide_and_conquer(numbers, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_cross(numbers, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

#Linear time algorithm
def algo4(arr):
    low_index = 0;
    high_index = 0;
    sub_sum = arr[0];
    max_sum = 0;

    for i in range(0,len(arr)-1):
        if(sub_sum + arr[i+1] > arr[i+1]):
            sub_sum += arr[i+1];
            if(sub_sum > max_sum):
                max_sum = sub_sum;
                high_index = i+1;
        else:
            sub_sum = arr[i+1];
            if(sub_sum > max_sum):
                max_sum = sub_sum;
                low_index = i+1;
                high_index = i+1;
    max_subarray = arr[low_index:(high_index+1)];
    print(arr);
    print(max_subarray);
    print(max_sum);
main()
