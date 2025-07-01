'''
Source:
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
'''

def is_leap(year: int) -> bool:
    '''
    Returns if the year is a leap year or not
    
    Args:
        year (int): number between 1900 and 10^5
        
    Returns:
        bool: leap year or not
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        
        return True
            
    return False

year = int(input())
print(is_leap(year))
