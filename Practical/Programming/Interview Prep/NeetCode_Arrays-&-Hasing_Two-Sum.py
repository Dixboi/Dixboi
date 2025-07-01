class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        https://neetcode.io/problems/two-integer-sum

        Args:
            nums List[int]: array of integers from -10,000,000
                up to 10,000,000
            target (int): the target value from -10,000,000
                up to 10,000,000
        
        Returns:
            List[int]: an array that contains the first and second
                index of integers that results the target
        '''
        difference = {}

        for i in range(len(nums)):
            diff = str(target - nums[i])

            if difference.get(diff, -1) == -1:
                difference[str(nums[i])] = i

            else:
                return [difference.get(diff, -1), i]
