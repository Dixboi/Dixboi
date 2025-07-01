'''
Source:
https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

Task:
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

Input Format:
The first and only line contains the integer, n.
'''

def function(n: int) -> list[int]:
    '''
    Return a list that contains the square
    of all positive integers that are less
    than the input

    Args:
        n (int): positive integer

    Returns:
        list[int]: a list of squares of the
                integers that are less than
                the input
    '''
    
    return [_**2 for _ in range(n)]

if __name__ == '__main__':
    n = int(input())
    for i in function(n):
        print(i)
