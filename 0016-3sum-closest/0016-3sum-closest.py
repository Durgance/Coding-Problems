class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
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
                    
                    if check_sum - target == 0  :
                        # l.append(sum([nums[i],nums[j],nums[k]]))
                        # j+=1
                        # print(f"{nums[i]} {nums[j]} {nums[k]}")
                        return check_sum
                        # so that no two same numbers can give problem
                        # while nums[j] == nums[j-1] and j<k:
                        #     j+=1
                    elif check_sum - target < 0:
                        l.append(check_sum)
                        j += 1
                    elif check_sum - target > 0:
                        l.append(check_sum)
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
        # print(l)
        return l[min(range(len(l)), key=lambda i: abs(l[i]- target))]
        # if len(l)==1:
        #     return l[0]
        # return min(l)+target
        # return sum(l)