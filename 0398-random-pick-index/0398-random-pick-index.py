class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.d = {}
        for i in range(len(self.nums)):
            if self.nums[i] not in self.d.keys():
                self.d[self.nums[i]] = [] 
            self.d[self.nums[i]].append(i)
        print(self.d) 

    def pick(self, target: int) -> int:
        
        return random.choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)