class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)

        for i in range(1,len(nums)):
            left_product[i] = left_product[i-1]*nums[i-1]
        # print(left_product)
        for i in range(len(nums)-2,-1,-1):
            right_product[i] = right_product[i+1] * nums[i+1]
        # print(right_product)
        for i in range(len(nums)):
            ans[i] = left_product[i]*right_product[i]
        
        return ans

        
        