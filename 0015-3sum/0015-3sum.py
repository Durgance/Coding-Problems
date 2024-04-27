class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l=[]
        # print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k = len(nums) - 1
            while j<k:
                # print([i,j,k])
                if i!=j and j!=k and i!=k :
                    check_sum = nums[i] + nums[j] + nums[k]
                    
                    if check_sum == 0 :
                        l.append([nums[i],nums[j],nums[k]])
                        j+=1
                        # so that no two name numbers can give problem
                        while nums[j] == nums[j-1] and j<k:
                            j+=1
                    elif check_sum < 0:
                        j += 1
                    elif check_sum > 0:
                        k -= 1  
                    
                else:
                    if i == j :
                        j+=1
                        continue
                    if i==k:
                        k-=1
                        continue
                    if j==k:
                        break
        
        return l
                