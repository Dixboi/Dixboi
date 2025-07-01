'''
https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        freqs = []

        for _ in range(1, len(nums)+1):
            bucket[_] = []
        
        nums_set = set(nums)
        for i in nums_set:
            bucket[nums.count(i)].append(i)
        
        bucket_count = len(bucket)
        while(len(freqs) < k):
            if len(bucket[bucket_count]) > 0:
                freqs = freqs + bucket[bucket_count]
            bucket_count -= 1
        
        return freqs
