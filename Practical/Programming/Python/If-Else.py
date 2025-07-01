'''
Source:
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

Task:
Given an integer, n, perform the following conditional actions:
- If n is odd, print `Weird`
- If n is even and in the inclusive range of  to , print `Not Weird`
- If n is even and in the inclusive range of  to , print `Weird`
- If n is even and greater than , print `Not Weird`

Input Format:
A single line containing a positive integer, .
'''

def function(n):
    if (n%2 != 0) or (6 <= n <= 20):
        return "Weird"
    
    if (2 <= n <= 5) or (n > 20):
        return "Not Weird"     

if __name__ == '__main__':
    n = int(input().strip())
    print(function(n))
