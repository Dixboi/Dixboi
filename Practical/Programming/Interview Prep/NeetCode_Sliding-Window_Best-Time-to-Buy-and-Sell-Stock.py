#
# https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_buy, profits = prices[0], [0]

        for i in range(1, len(prices)):
            if prices[i] < curr_buy and i != len(prices) - 1:
                curr_buy = prices[i]
            else:
                profits.append(prices[i] - curr_buy)
        
        return max(profits)
