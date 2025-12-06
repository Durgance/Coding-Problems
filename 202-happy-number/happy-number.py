class Solution:
    def get_sum(self, num):
        s = 0
        while num!=0:
            digit = num%10
            s += digit**2
            num = num//10
        return s
    
    def isHappy(self, n: int) -> bool:
        count = 0
        while True:
            val = self.get_sum(n)
            if val ==1:
                return True
            n = val
            if count>=10:
                return False
            count +=1
        return False