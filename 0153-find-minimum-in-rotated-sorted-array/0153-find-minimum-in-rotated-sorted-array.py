class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 3:
            return min(nums)
        while left<right:
            mid = left + ((right -left)//2)
            if nums[mid] > nums[left] and nums[mid] < nums[right]:
                return nums[left]
            elif nums[mid] < nums[left]:
                right = mid 
            elif nums[mid] > nums[left]:
                left = mid
            elif nums[mid] == nums[left]:
                # print(nums[mid-1])
                # print(nums[mid])
                # print(nums[mid+1])
                return min(nums[mid-1],nums[mid],nums[mid+1])
        
        
        
            