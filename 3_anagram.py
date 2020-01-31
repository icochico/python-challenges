# Given two strings s1 and s2 in input, detect if s2 is an "anagram" of s2
# An anagram is a string of the same lenght with the same exact number of characters but in different order

# requirements
# Assume the strings given in input can have arbitrary length
# Assume no spaces
# Assume lowercase and uppercase are the same letter
from collections import Counter

# solution in O(logn) time
def is_anagram_1(s1: str, s2: str) -> bool:
    
    if len(s1) != len(s2):
        return False
    
    # sanitiziation
    s1 = s1.lower()
    s2 = s2.lower()

    # sorting
    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

# solution in O(nlogn) time
def is_anagram_2(s1: str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False

    # sanitiziation
    s1 = s1.lower()
    s2 = s2.lower()

    c1 = Counter(s1)
    c2 = Counter(s2)

    if c1 == c2:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_anagram_1("pale", "lepa"))
    print(is_anagram_1("pamee", "mmepa"))
    print(is_anagram_2("pale", "lepa"))
    print(is_anagram_2("pamee", "mmepa"))
