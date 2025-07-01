'''
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
'''

if __name__ == '__main__':
    
    records = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    
    min_ = min(records.values())
    sec_min = 100
    for val in records.values():
        if (min_ < val) and (val < sec_min):
            sec_min = val
    
    names = []        
    for key, val_ in records.items():
        if val_ == sec_min:
            names.append(key)
    
    names.sort()
    for m in names:
        print(m)
        
        
