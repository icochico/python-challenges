# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
# Complete the function sherlockAndAnagrams in the editor below. 
# It must return an integer that represents the number of anagrammatic pairs of substrings in s.

import math
import os
import random
import re
import sys
from collections import Counter

# Divide problem in 2 subproblems
# Traverse all possible substrings within string
# Check if any two substrings of equal length are anagrams
def sherlockAndAnagrams(s: str) -> int:

    count = 0
    for i in range(1, len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b: 
            # making combinations of size 2
            count+=b[j]*(b[j]-1)/2
    return int(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()