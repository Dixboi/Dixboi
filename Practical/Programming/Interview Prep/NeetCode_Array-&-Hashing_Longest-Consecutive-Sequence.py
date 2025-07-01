#
# https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
#

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = {}

        for i in nums:
            if i-1 not in nums:
                hash_set[i] = [i]
            
                inc = 1
                while True:
                    if i+inc in nums:
                        hash_set[i].append(i+inc)
                        inc += 1
                    else:
                        break
        
        best = 0
        for j in hash_set.values():
            if len(j) > best:
                best = len(j)
        
        return best
