class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start ,end , win_sum = 0, 0, 0
        min_len = float('inf')
        # flag = False
        for end in range(len(nums)):
            win_sum += nums[end]
            while win_sum>=target:
                # flag = True
                win_sum -= nums[start]
                min_len = min(min_len,end-start+1)
                start+=1
                # end = start
                # win_sum = 0
            # else:
            #     end+=1
        # if flag == False:
        #     return 0
        # else:
        #     return min_len
        return min_len if min_len != float('inf') else 0
