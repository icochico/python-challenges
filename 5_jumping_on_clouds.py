# Emma is playing a new mobile game that starts with consecutively numbered clouds. 
# Some of the clouds are thunderheads and others are cumulus. 
# She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
# She must avoid the thunderheads. 
# Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. 
# It is always possible to win the game.
# Output Format

# Print the minimum number of jumps needed to win the game.
# Sample Input 0
# 7
# 0 0 1 0 0 1 0
# Sample Output 0
# 4

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jumps = 0
    i = 0
    while i < len(c):

        if i == len(c)-1:
            break

        # check if we are not to close to the end of the array to jump 2
        if i < len(c)-2 and c[i+2] == 0:
            i += 2
        else:
            i += 1

        jumps += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()