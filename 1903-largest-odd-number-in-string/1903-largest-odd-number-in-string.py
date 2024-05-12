class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_num = 0
        left = 0
        right = len(num)-1
        if len(num) == 1:
            if int(num)%2!=0:
                return num
            return "" 
        while True:
            if int(num[right]) %2 != 0:
                return num[:right+1]
            else:
                right-=1
            if left == right :
                if int(num[left])%2 !=0:
                    return num[left]
                break
        return ""