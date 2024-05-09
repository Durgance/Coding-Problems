class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        # buy_price = prices[0]
        # sell_price = 0
        # # flag = False
        # amount = []
        # profit = 0
        # for i in range(len(prices)):
        #     if prices[i] <= buy_price:
        #         buy_price = prices[i]
        #         buy_idx = i
        #     elif prices[i] > buy_price:
        #         if prices[i]>=sell_price or buy_idx > sell_idx:
        #             sell_price = prices[i]
        #             sell_idx = i
                    
        #         if sell_idx > buy_idx:
        #             profit = max(profit,sell_price-buy_price)
        #             amount.append(profit)
        #             # sell_price = 0
        # if len(amount) == 0:
        #     return 0
        # print(amount)
        # return max(amount)
        left = 0
        right = 0
        max_profit = 0
        total_profit = 0
        while right<len(prices) and left<len(prices):
            profit = prices[right] - prices[left]
            # print(f"{left} {right} {profit} {max_profit} {total_profit}")
            if left == right:
                right+=1
                continue
            if profit < max_profit :
                # left += 1
                total_profit += max_profit
                # if profit > 0:
                max_profit = 0
                left=right
                continue
            if profit > 0:
                # print("R")
                max_profit = max(profit,max_profit)
                if right == len(prices)-1:
                    # print("E")
                    total_profit += max_profit
                    break
            right += 1

        if total_profit == 0 and max_profit != 0:
            return max_profit 
        return total_profit