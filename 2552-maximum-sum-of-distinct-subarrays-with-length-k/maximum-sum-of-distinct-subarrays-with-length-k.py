class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        max_sum = 0
        win_sum = 0
        n = len(nums)
        num_freq = {}
        for end in range(n):
            right_win = nums[end]
            # max_sum += right_win
            
            num_freq[right_win] = 1 + num_freq.get(right_win,0)
            
            # if right_win in num_freq:
            win_sum += right_win

            while len(num_freq) >= k :
                
                left_win = nums[start]
                # print(nums[start:end+1])
                if end-start + 1 == k:
                    max_sum = max(max_sum,win_sum)
                win_sum -=  left_win
                start+=1
                
                num_freq[left_win] -= 1
                if num_freq[left_win] == 0 :
                    del num_freq[left_win]

        return max_sum
