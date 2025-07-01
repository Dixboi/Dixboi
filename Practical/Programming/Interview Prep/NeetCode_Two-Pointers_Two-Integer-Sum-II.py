#
# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150
#

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            partner = target - numbers[i]
            if partner in numbers[i:]:
                idx_partner = numbers.index(partner)
                if i != idx_partner:
                    return [i+1, idx_partner+1]
