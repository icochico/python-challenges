# Given two strings, determine if they share a common substring. A substring may be as small as one character.
# For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring.

import math
import os
import random
import re
import sys
from collections import Counter

# time complexity O(n)
# space complexity O(n)
def twoStrings(s1: str, s2: str) -> str:

    c1 = Counter(s1)

    for ch in s2:
        if ch in c1:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()