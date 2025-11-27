class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return len(nums)
        # if len(set(nums)) == len(nums):
        #     return len(nums)
        p = 2
        loc = 2
        # for i in range(2,len(nums)):
        while p<len(nums):
            # print(left,right)
            # if nums[left]>nums[right]:
            #     break
            if nums[p] != nums[loc - 2] :
                nums[loc] = nums[p]
                loc+=1
                # left = 0
            p+=1
            if p>=len(nums):
                break
        # print(nums)
        return loc
