class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        buy_price = prices[0]
        sell_price = 0
        # flag = False
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= buy_price:
                buy_price = prices[i]
                buy_idx = i
            elif prices[i] > buy_price:
                if prices[i]>=sell_price or buy_idx > sell_idx:
                    sell_price = prices[i]
                    sell_idx = i
                    
                if sell_idx > buy_idx:
                    profit = max(profit,sell_price-buy_price)
                    # sell_price = 0
        if sell_price == 0:
            return 0
        else :
            return profit