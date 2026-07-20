class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_stock = min(min_stock, prices[i])
            max_profit = max(max_profit, prices[i]- min_stock)
        return max_profit