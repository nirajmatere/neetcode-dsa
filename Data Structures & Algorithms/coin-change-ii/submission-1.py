class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # coins.sort()
        memo = {}

        def dfs(i,curr_amount):
            if curr_amount == 0:
                return 1
            if i >= len(coins) or curr_amount < 0:
                return 0

            if (i, curr_amount) in memo:
                return memo[(i,curr_amount)]

            keep = dfs(i, curr_amount - coins[i])
            not_keep = dfs(i+1, curr_amount)

            memo[(i,curr_amount)] = keep + not_keep
            return memo[(i,curr_amount)]

        return dfs(0,amount)
        