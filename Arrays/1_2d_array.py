# Given a 6x6 2D Array:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in A to be a subset of values with indices 
# falling in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr, and an hourglass sum is the sum of 
# an hourglass' values. Calculate the hourglass sum for every hourglass in arr, 
# then print the maximum hourglass sum.

# Complete the function hourglassSum in the editor below. 
# It should return an integer, the maximum hourglass sum in the array.

# hourglassSum has the following parameter(s):

# arr: an array of integers

#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def hourglassSum(arr):

    # want to find the maximum hourglass sum
    # minimum hourglass sum = -9 * 7 = -63
    max = -63
    
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            hourglass = (arr[i][j] + 
                        arr[i-1][j-1] + 
                        arr[i-1][j] +
                        arr[i-1][j+1] +
                        arr[i+1][j-1] + 
                        arr[i+1][j] + 
                        arr[i+1][j+1])
            
            if hourglass > max:
                max = hourglass
    
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

