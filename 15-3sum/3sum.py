class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        triplets = []
        # TODO: Write your code here
        arr.sort()
        # print(arr)
        i = 0
        # left = 0
        right = len(arr) - 1
        for i in range(len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                continue
            if arr[i]>0:
                break

            target = -1*arr[i]
            left = i+1
            right = len(arr) - 1
            while left<right:
                curr_sum = arr[left] +arr[right]
                if curr_sum == target:
                    triplets.append([arr[i],arr[left],arr[right]])
                    # print(triplets)
                    left += 1
                    right -= 1
                    while left<right and arr[left]==arr[left-1]:
                        left += 1
                    while left<right and arr[right]==arr[right+1]:
                        right -= 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
                # right = len(arr) - 1

            # i += 1
        return triplets
