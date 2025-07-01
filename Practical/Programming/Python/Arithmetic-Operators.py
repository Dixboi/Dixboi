'''
Source:
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

Task:
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

- The first line contains the sum of the two numbers.
- The second line contains the difference of the two numbers (first - second).
- The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer, a.
The second line contains the second integer, b.
'''

def function(a: int, b: int) -> list[int]:
	'''
    Return a list that contains the sum,
    difference, and product of a and b.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        list[int]: containts the sum, difference,
                and product
    '''
    
    return [a+b, a-b, a*b]

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = function(a, b)
    print(c[0])
    print(c[1])
    print(c[2])
