class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        max_profit = 0
        profit = 0
        while R < len(prices):
            if prices[R] < prices[L]:
                L = R
            else:
                profit = prices[R] - prices[L]
                if profit > max_profit:
                    max_profit = profit
            R += 1
        return max_profit