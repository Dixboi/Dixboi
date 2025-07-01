# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
#
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

def get_ratio(count_: int, arr_len: int) -> float:
    return "{:.6f}".format(round(count_ / arr_len, 6))

def plusMinus(arr: list[int]) -> None:
    arr_len = len(arr)
    pos, neg, zer = 0, 0, 0
    
    for _ in arr:
        if _ > 0: # positives
            pos += 1
        elif _ < 0: # negatives
            neg += 1
        else: # zeroes
            zer += 1
    
    pos_rat = get_ratio(pos, arr_len)
    neg_rat = get_ratio(neg, arr_len)
    zer_rat = get_ratio(zer, arr_len)
    
    print(pos_rat)
    print(neg_rat)
    print(zer_rat)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
