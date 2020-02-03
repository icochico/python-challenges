# You are given a string containing characters A and B only. 
# Your task is to change it into a string such that there are no matching adjacent characters. 
# To do this, you are allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.
# Complete the alternatingCharacters function in the editor below. 
# It must return an integer representing the minimum number of deletions to make the alternating string.

# alternatingCharacters has the following parameter(s):
# s: a string

#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity: O(n)
# Space Complexity: O(n)
def alternatingCharacters(s: str) -> int: 

    previous = ''
    num_deletes = 0
    for c in s:
        if (c == previous):
            num_deletes += 1
        previous = c

    return num_deletes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()