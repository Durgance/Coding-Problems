class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        left = 0
        right = 0
        max_profit = 0
        while right<len(prices):
            # print(f"{left} {right}")
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                continue
            if profit>0:
                max_profit = max(max_profit,profit)
            right += 1
        return max_profit

