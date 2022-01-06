#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    ans = []
    trie = {} # dictionary in dictionary for binary tree of bits for every number in array
    # node copies from trie and is for further processing
    k = len(bin(max(arr+queries))) - 2 # longest binary length, 2 is for ob prefix
    for binumber in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie # update node as trie was updated by setdefault
        #print(f'binumber is {binumber}')
        for bit in binumber:
            node = node.setdefault(bit, {}) # bc it is dict, it also changes trie
        #print(f'{trie}')
    for n in queries: # 3 7 2
        node = trie
        s = ''
        for bit in'{:b}'.format(n).zfill(k) : # 011,111,010
            #print(f'node {node}')
            reversebit = str(int(bit) ^ 1) # flipping the bits
            reversebit = reversebit if reversebit in node else bit
            s += reversebit
            node = node[reversebit] # go inside another tree
        ans.append(int(s, 2) ^ n) # convert from base 2 to integer
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
