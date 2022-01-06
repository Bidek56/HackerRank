#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/triple-sum

# Complete the triplets function below.
from bisect import bisect

def triplets(a, b, c):
    a, b, c = sorted(set(a)), set(b), sorted(set(c))
    return sum((bisect(a, x) * bisect(c, x) for x in b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
