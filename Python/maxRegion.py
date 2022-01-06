#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

def size(i,j):
    if (i in range(n)) and (j in range(m)) and grid[i][j] ==1:
        grid[i][j]=0
        return 1 + sum(size(i2,j2) for i2 in range(i-1,i+2) for j2 in range(j-1,j+2))
    return 0
def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    return max(size(i,j) for i in range(n) for j in range(m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
