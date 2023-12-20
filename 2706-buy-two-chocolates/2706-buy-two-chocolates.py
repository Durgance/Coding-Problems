class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        for i in range(len(prices)):
            l_m = money-prices[i]
            if l_m <= 0:
                return money
            for j in range(len(prices)):
                if i!=j and prices[j] <= l_m:
                    return money-(prices[i]+prices[j])
        return money
                
        

