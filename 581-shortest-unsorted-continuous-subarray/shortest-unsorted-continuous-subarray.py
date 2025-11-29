class Solution:
        

    def findUnsortedSubarray(self, nums: List[int]) -> int:
            # print(nums)
            # TODO: Write your code here
            l = 0
            r = 1
            start = 0
            while r<len(nums):
                if nums[l]<=nums[r]:
                    l+=1
                    r+=1
                elif nums[l]>nums[r]:
                    start = l
                    break
            # if array is sorted then should reach the length of the array
            if l == len(nums) -1 :
                return 0

            l = len(nums)-2
            r = len(nums)-1
            end = 0
            while l>=0:
                if nums[l]<=nums[r]:
                    l-=1
                    r-=1
                elif nums[l]>nums[r]:
                    end=r
                    break
            # print(f"({start},{nums[start]}) : ({end},{nums[end]}) ")

            # now i know the start and end of the subarray if possible this result 
            # need to extend the array if needed in both direction
            # now i need to min of the sub array  and maximum value in the sub array
            min_subarray = math.inf
            max_subarray = -math.inf

            for value in range(start,end+1):
                min_subarray = min(min_subarray,nums[value])
                max_subarray = max(max_subarray,nums[value])
            
            # print(f"(MAX : {max_subarray}) , (MIN : {min_subarray}) ")
            
            while start>0:
                if nums[max(start-1,0)]>min_subarray :
                    start=max(start-1,0)
                else:
                    break
            while end<len(nums) :
                if nums[min(end+1,len(nums)-1)]<max_subarray :
                    end = min(end+1,len(nums))
                else :
                    break
            
            # print(f"({start},{nums[start]}) : ({end},{nums[min(end,len(nums)-1)]}) ")
            # print(f"(MAX : {max_subarray}) , (MIN : {min_subarray}) ")
            # print("------------------------------")
            # print("------------------------------")
            # print("------------------------------")
            return abs(min(end,len(nums)-1)-start)+1