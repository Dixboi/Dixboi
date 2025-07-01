'''
Source:
https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

Task:
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

Input Format:
The first line contains the first integer, a.
The second line contains the second integer, b.

'''

def function(a: int, b: int) -> list[int | float]:
    '''
    Return a list that contains the integer
    and float quotient of a and b

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        list[int | float]: containts integer
                        and float quotient
    '''
    
    return [a // b, a / b]

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = function(a, b)
    print(c[0])
    print(c[1])
