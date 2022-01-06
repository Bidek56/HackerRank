#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
# https://www.hackerrank.com/challenges/sock-merchant

input()
socks, pairs = Counter(map(int,input().strip().split())), 0
for s in socks: pairs += socks[s]//2
print(pairs)
