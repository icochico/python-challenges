# given an array of integers, return an array containing the integer that occurs the least 
# number of times. If there are multiple answers, return all possibilities within the 
# resulting array, sorted in ascending order. When no solution can be deduced, return an 
# empty array

from collections import Counter 

def solution(numbers):
    
    if len(numbers) == 0:
        return []
    
    c = Counter(numbers)        
    # get least common
    least_common = c.most_common()[:-2:-1]
    # get value if non empty
    min = least_common[0][1]
    result = []
    for key in c.keys():
       if c[key] == min:
           result.append(key)
         
    result.sort()
    
    return result
