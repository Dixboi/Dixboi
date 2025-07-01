def function(arr: list[int]) -> int:
	'''
 	https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
  	'''
    arr = list(arr)
    max_ = max(arr)
    value = min(arr)
    for i in arr:
        if i > value and i < max_:
            value = i
    return value
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(function(arr))
