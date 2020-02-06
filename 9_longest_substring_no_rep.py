# Given a string s, find the length of the longest substring that contains no repeated characters
# e.g. 
# Input:
# s: "nndfddf"
# Your Output:
# 3

def solution(s):
    
    record_lon = 0
    longest = ""
    for c in s:
        if c in longest:
            if len(longest) > record_lon:
                record_lon = len(longest)
            
            # clear longest by resetting starting from first duplicated char + 1 
            longest = longest[longest.index(c)+1:]
         
        longest += c
        
    # verify last case
    if len(longest) > record_lon:
        record_lon = len(longest)
    
    return record_lon