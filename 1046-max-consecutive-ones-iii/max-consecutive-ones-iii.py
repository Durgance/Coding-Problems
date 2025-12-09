class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len , max_ones_count , start = 0 ,0 ,0 
        # freq_map = {}
        # zero_counter = 0
        n = len(nums)
        for end in range(n):
            if nums[end] == 1 : max_ones_count +=1
            
            # right_num = nums[end]
            # freq_map[right_num] = 1 + freq_map.get(right_num,0)
            # # Need to get the number of 1st list so that i can get the number of zeros to flip
            # max_ones_len = max(max_ones_len,freq_map.get(1,0))

            # setting the condition to shift the window 
            # Generalized solution when getting max consecutive 
            # window_len - max_char > k 
            # if (end - start + 1 - max_ones_len) > k:
            #     left_num = nums[start]
            #     freq_map[left_num] -= 1
            #     start += 1
            # print(f"Start : {start} , End : {end}, Len : {end - start +1} , max_ones : {max_ones_len}")
            # print(start)
            # print(end-start +1)
            while (end - start +1 - max_ones_count) > k:
                if nums[start] == 1:
                    max_ones_count -=1
                start+=1
            # if zero_counter > k:
            #     zero_counter -=1
            #     start +=1

            max_len = max(max_len , end - start +1 )
        return max_len