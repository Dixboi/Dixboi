def function(x: int, y: int, z: int, n: int) -> list[list[int]]:
    '''
    https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
    '''
    
    lists = [[i, j, k] for k in range(z+1) for j in range(y+1) for i in range(x+1) if (i + j + k) != n]
    lists.sort()
    return lists
                

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(function(x,y,z,n))
