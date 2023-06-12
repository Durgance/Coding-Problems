class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums :
            return []
        start = 0
        end = 0
        pointer = 1
        ans = []
        while pointer<len(nums):  
            if (nums[pointer]-nums[pointer-1])<=1:
                pointer += 1
                # print(pointer)
                continue
            if (nums[start]==nums[pointer-1]):
                ans.append(f"{nums[start]}")
            else:    
                ans.append(f"{nums[start]}->{nums[pointer-1]}")
            # print(f"{start} : {pointer}")
            start = pointer
            pointer += 1
        if (nums[start]==nums[len(nums)-1]):
            ans.append(f"{nums[start]}")
        else:    
            ans.append(f"{nums[start]}->{nums[pointer-1]}")
            
        
        return ans
            
        
        