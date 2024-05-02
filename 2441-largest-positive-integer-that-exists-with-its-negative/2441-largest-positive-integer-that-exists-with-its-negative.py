class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}
        ans = []
        for num in nums:
            if not d.get(num) :
                d[num] = 1
            if d.get(-1*num):
                ans.append(abs(num))
        if len(ans)==0:
            return -1
        return max(ans)
        