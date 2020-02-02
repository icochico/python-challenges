# Complete the repeatedString function in the editor below. 
# It should return an integer representing the number of occurrences of a 
# in the prefix of length n in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider

# Sample Input 0
# aba
# 10

# Sample Output 0
# 7

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    #s_rep = repeat_to_length(s, n)
    count_a = 0
    for c in s:
        if c == 'a':
            count_a += 1
    
    # calculate reps and leftover char length of n-th repeated string
    reps = n // len(s) # floor
    leftover = n % len(s) # mod 

    total_count_a = count_a * reps

    # count extra in the last leftover string
    extra = 0
    i = 0
    while i < leftover:
        if c == 'a':
            extra += 1
        i += 1

    total_count_a = total_count_a + extra

    return total_count_a

def repeatedStringCompact(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()