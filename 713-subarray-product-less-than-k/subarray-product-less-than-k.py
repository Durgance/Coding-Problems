class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        n = len(nums)
        max_win_product = 1
        # res = []
        win_len = 0
        if k ==0 : 
            return 0
        for end in range(n):
            right_nums = nums[end]
            max_win_product *= right_nums

            while max_win_product >= k and start<=end:
                left_nums = nums[start]
                max_win_product //= left_nums
                start += 1
            win_len += end - start +1
            # res.append((nums[start: end +1],max_win_product))
        # print(res)
        return win_len

