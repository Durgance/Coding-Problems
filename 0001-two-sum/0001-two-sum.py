class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        
        for i in range(len(nums)):
            x = nums[i]
            y= target - x
            test = nums[:i]+nums[i+1:]
            # print(test)
            try :
                check = test.index(y)

                if (check+1) !=i:
                    return i,check+1
            except :
                continue