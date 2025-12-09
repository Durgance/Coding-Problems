class Solution:

    def at_most(self,arr,k):
        start = 0
        # counter += 1
        count_odd = 0
        result = 0
        n = len(arr)
        for end in range(n):
            right_win = arr[end]

            if right_win%2 !=0:
                count_odd += 1

            while count_odd >k  and start<=end:
                left_win = arr[start]
                if left_win %2 != 0 :
                    count_odd -= 1
                start +=1
            result += end - start +1
        return result


    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # start , max_len  = 0, 0
        # n = len(nums)
        # count_odd = 0
        # counter = 0
        # for end in range(n):
        #     right_win = nums[end]
            
        #     if right_win%2!=0:
        #         count_odd +=1
            
        exactly_k = self.at_most(nums,k) - self.at_most(nums,k-1)


        return exactly_k
            