class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(n, state):
            if n >= len(prices):
                return 0
            if (n, state) in memo:
                return memo[(n,state)]
            if state == 'can_buy':
                buy = dp(n+1, 'can_sell') - prices[n]
                not_buy = dp(n+1, 'can_buy')
                memo[(n, 'can_buy')] = max(buy, not_buy)
                return memo[(n, 'can_buy')]
            elif state == 'can_sell':
                sell = dp(n+2, 'can_buy') + prices[n]
                not_sell = dp(n+1, 'can_sell')
                memo[(n, 'can_sell')] = max(sell, not_sell)
                return memo[(n, 'can_sell')]

        return dp(0, 'can_buy')