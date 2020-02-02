# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

# n: the number of socks in the pile
# ar: the colors of each sock

import math
import os
import random
import re
import sys
from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(n)
def sockMerchant1(n, ar):
    
    socks = {}
    for color in ar: 
        count = socks.get(color, 0)
        count += 1
        socks[color] = count

    matching = 0
    for color in socks:
        matching += socks[color] // 2

    return matching


# Time Complexity: O(n)
# Space Complexity: O(n)
def sockMerchant2(n, ar):
    # Counter automates dictionary lookup
    socks = Counter(ar)
    matching = 0
    for color in socks:
        matching += socks[color] // 2
    
    return matching


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant1(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
