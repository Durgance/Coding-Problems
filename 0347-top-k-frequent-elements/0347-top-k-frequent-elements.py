class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums = Counter(nums)
        nums = sorted(nums, key = nums.get, reverse=True)
        return nums[:k]
        