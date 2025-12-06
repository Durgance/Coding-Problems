class Solution:
    def get_sum(self, num):
        s = 0
        while num!=0:
            digit = num%10
            s += digit**2
            num = num//10
        return s
    
    def isHappy(self, n: int) -> bool:
        # count = 0
        slow ,fast = n, n
        while True:
            slow = self.get_sum(slow)
            fast = self.get_sum(fast)
            fast = self.get_sum(fast)

            if slow ==1 or fast == 1:
                return True
            elif slow == fast:
                return False
            # n = val
            # if count>=10:
            #     return False
            # count +=1
        # return False