class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for price in prices:
            if price <= buy_price:
                buy_price = price
            else:
                profit = price - buy_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit