# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    cnt_pos,cnt_neg,cnt_zero = 0,0,0
    for num in arr:
        if num > 0: cnt_pos = cnt_pos + 1
        elif num == 0: cnt_zero = cnt_zero + 1
        else: cnt_neg = cnt_neg + 1
    
    print(f"{cnt_pos/length:.6f}", f"{cnt_neg/length:.6f}", f"{cnt_zero/length:.6f}", sep="\n")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
