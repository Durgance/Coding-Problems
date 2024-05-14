class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        # return sorted(list(enumerate(nums)),key=lambda x:x[1])[-1][0]
        if len(nums) == 1:
            return 0
        
        low = 1
        high = len(nums) -2
        if nums[0]>nums[low]:
            return 0
        if nums[high +1]>nums[high]:
            return high+1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                low = mid + 1
            else:
                high = mid-1
        return -1