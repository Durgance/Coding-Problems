class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sorted(list(enumerate(Counter(nums).items())),key = lambda x: x[1][1])[0][1][0]
        