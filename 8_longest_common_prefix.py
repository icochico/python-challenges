# Given an array of strings, strings, find the longest common prefix among all the strings. 
# If there is no prefix that all the strings share, return the empty string ""
# E.g.
# strings: ["abcdef","abcghi","abcabc"]
# Your Output:
# "abc"


def solution(strings):
    
    if len(strings) == 0:
        return ""
    
    # find shortest string for the longes common prefix:
    shortest_len = len(min(strings, key=len))
    
    prefix = ""
    prefix_can = ""
    j = 0;
    while j < shortest_len:
        for string in strings:
            if prefix_can == "":
                prefix_can = string[j]
            elif string[j] != prefix_can:
                return prefix
            
        # if all strings have the char, update prefix
        prefix = "".join((prefix, prefix_can))
        # reset prefix candidate
        prefix_can = ""
        j+=1
        
    return prefix
