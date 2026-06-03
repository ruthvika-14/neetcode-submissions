class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profit = 0

        for prices in prices:
            min_prices = min(prices, min_prices)
            profit = prices - min_prices
            max_profit = max(max_profit, profit)

        return max_profit       