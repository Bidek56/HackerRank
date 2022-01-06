#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/max-array-sum

# Using tabulation (bottom up approach) 
# Note that in the dp dictionary, we store the max sum for the subarray up till the length of the subarray. Hence, we simply return the last item in this dictionary to get the answer

def maxSubsetSum(arr):
    dp = {} # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
