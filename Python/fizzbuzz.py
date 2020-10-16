
import math
import os
import random
import re
import sys

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
def fizzBuzz(n):
    for fizzbuzz in range(1,n):
        print(f"N: {fizzbuzz}")
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        print(fizzbuzz)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)