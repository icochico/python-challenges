# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
# Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# time complexity O(n)
# space complexity O(n)
def isValid(s: str) -> bool:

    # pre checks
    if (s == ""):
        return "NO"
    
    if (len(s) <= 3):
        return "YES"

    c = Counter(s)
    counts = list(c.values())
    max_c = max(counts)
    min_c = min(counts)

    # if they are the same, all characters appear with the same frequency
    if (max_c == min_c):
        return "YES"
    
    # if max-min difference greater than 1, one or more characters prevail over the others
    if (max_c - min_c > 1):
        return "NO"
    
    # otherwise, count how max and min
    max_num = 0
    min_num = 0
    for num in counts:
        if num == max_c:
            max_num += 1
        else:
            min_num += 1

    # if any of max and min equals 1, string is still valid
    if max_num == 1 or min_num == 1:
        return "YES"
    else:
        return "NO"       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
