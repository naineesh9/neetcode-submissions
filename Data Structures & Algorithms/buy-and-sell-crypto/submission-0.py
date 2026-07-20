class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if diff < prices[j] - prices[i]:
                    diff = prices[j] - prices[i]
        return diff