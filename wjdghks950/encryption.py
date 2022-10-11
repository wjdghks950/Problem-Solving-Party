#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    l = len(s)
    col = math.ceil(math.sqrt(l))
    row = math.floor(math.sqrt(l))
    if l > col**2 - col:
        row = col
    ans = ""
    for c in range(col):
        ans += s[c]
        if l <= c + ((row-1) * col):
            row = row - 1
        for r in range(1,row):
            ans = ans + s[c + (r * col)]
        ans += " "
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

