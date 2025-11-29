class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        rem = sum(nums) % k
        return rem
        if rem == 0 :
            return 0
        else :
            m = max(nums)
            
            if m>=rem:
                return rem
            # elif m<rem:

            else:
                # return sum(nums)
                c = 0
                if sum(nums)<k:
                    return sum(nums)
                while True:
                    # m = max(nums)
                    # if m>=rem:
                    #     idx = nums.index(m)
                    idx = nums.index(m)
                    c += nums[idx]
                    rem -= nums[idx]
                    nums[idx] = 0
                    if rem-max(nums)>0:
                        continue
                        pass
                    else:
                        return c + rem
                        # rem = max(nums[idx])
                    #     return nums[idx]





