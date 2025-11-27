class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return len(nums)
        # if len(set(nums)) == len(nums):
        #     return len(nums)
        left = 2
        right = 2
        # for i in range(2,len(nums)):
        while left<len(nums):
            # print(left,right)
            # if nums[left]>nums[right]:
            #     break
            if nums[left] != nums[right - 2] :
                nums[right] = nums[left]
                right+=1
                # left = 0
            left+=1
            if left>=len(nums):
                break
        # print(nums)
        return right
