class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        starting_amount = amount
        def dfs(amount, dp):
            if amount == 0:
                return 0
            if amount <= -1:
                return float("inf")
            
            if dp[amount] != -1:
                return dp[amount]

            dp[amount] = float("inf")

            for a in coins:
                dp[amount] = min(dp[amount], 1 + dfs(amount - a, dp))
            return dp[amount]
        
        
        res = dfs(amount, [-1] * (amount + 1))
        return res if res != float("inf") else -1