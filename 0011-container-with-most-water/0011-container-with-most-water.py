class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) -1 
        maxA = 0
        while left<right:
            currA = min(height[left],height[right])*(right-left)
            maxA = max(maxA,currA)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxA