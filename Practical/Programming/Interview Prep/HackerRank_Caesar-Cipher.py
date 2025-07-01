# https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = lowers.upper()
    ciphered = ""
    
    for _ in s:
        if _ not in lowers and _ not in uppers:
            ciphered += _
        else:
            if _.upper() == _:
                ciphered += uppers[(uppers.find(_) + k) % len(uppers)]
            else:
                ciphered += lowers[(lowers.find(_) + k) % len(lowers)] 
    
    return ciphered

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
