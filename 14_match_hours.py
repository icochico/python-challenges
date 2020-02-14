# Given a series of meeting times, find the time slot that is available to everyone.
# work hours: 9-18
#
# e.g. 
# a = [9,13,14,17]
# b = [8,11,13,16]
# c = [8,9,11,13,16]
# d = [8,11,14,16]

from collections import Counter

def find_matching_hours(a: list, b: list, c: list, d: list) -> set:
    
    f = list(range(8,18))
    match = set(f) - set(a) - set(b) - set(c) - set(d)

    return match

if __name__ == '__main__':

    a = input()
    b = input()
    c = input()
    d = input()
    
    result = find_matching_hours(a, b, c, d)
    print(f"Matching schedule is {result}")
    
