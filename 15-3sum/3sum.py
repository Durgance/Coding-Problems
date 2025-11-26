class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        nums.sort()
        i = 0
        while i<len(nums):
            target = -1*nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                curr_sum = nums[left] + nums[right]
                if curr_sum<target:
                    left+=1
                elif curr_sum>target:
                    right-=1
                else:
                    triplets.add((nums[i],nums[left],nums[right]))
                    left+=1
            i+=1
        return list(map(list,triplets))