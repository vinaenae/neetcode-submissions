class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit = 0, 0
        buy = prices[left]
        if len(prices) > 1:
            for R in range(1, len(prices)):
                sell = prices[R]
                if sell < buy:
                    left = R
                    buy = prices[R]
                    curr_total = buy
                else:
                    curr_total = sell - buy
                    max_profit = max(max_profit, curr_total)
        else:
            return 0
        return max_profit           
            

        

        