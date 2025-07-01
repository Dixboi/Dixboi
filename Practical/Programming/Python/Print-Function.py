'''
https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
'''

def function(n: int) -> str:
    '''
    Returns a string from 1 to n without spaces
    
    Args:
        n (int): a positive integer
        
    Returns:
        a string from 1 to n without any spaces
    '''
    return [print(str(i+1), end="") for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    function(n)
