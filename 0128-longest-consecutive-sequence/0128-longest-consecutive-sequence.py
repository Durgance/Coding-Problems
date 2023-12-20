class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)
        # nums= list(set(nums))
        import heapq
        heapq.heapify(nums)
        curr_value = heapq.heappop(nums)
        count = 1
        ans = 1
        while True:
            try:
                next_value = heapq.heappop(nums)
            except Exception as e:
                    break
            if next_value-curr_value == 1:
                count += 1
                ans = max(count,ans)
            elif next_value-curr_value == 0:
                pass
            else:
                count = 1
                
            curr_value = next_value
        return ans
            
