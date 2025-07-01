"""
https://neetcode.io/problems/duplicate-integer
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Check if there is a duplicate in the list

        Args:
            nums List[int]: contains integers
        
        Returns:
            bool: will return true if there is a
                duplicate, otherwise false

        INITIAL SOLUTION
        ```
        return len(set(nums)) != len(nums)
        ```

        '''
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            
            hashset.add(i)
        
        return False
         
