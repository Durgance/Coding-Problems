
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # return sum([abs(num-nums[len(nums)//2]) for num in nums])
        if len(nums)%2 != 0:
            m1 = nums[len(nums)//2]
            return sum(list(map(lambda x: abs(x-m1),nums)))
        else:
            m1 , m2 = nums[len(nums)//2-1] , nums[len(nums)//2]
            return min(sum(list(map(lambda x: abs(x-m1),nums))),sum(list(map(lambda x: abs(x-m2),nums))))
