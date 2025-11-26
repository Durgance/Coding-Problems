class Solution:
    def threeSumClosest(self, arr: List[int], target_sum: int) -> int:
        arr.sort()
        score = float('inf')
        # print(arr)
        for i in range(len(arr)-2):
            target = arr[i]
            left = i+1
            right = len(arr)-1
            # score = min(score,abs(target_sum-target))
            while left<right:
                total = arr[left]+arr[right] + arr[i]
                if total<target_sum:
                # score = min(score,abs(target_sum-total))
                    if score >= abs(target_sum-total):
                        score = min(score,abs(target_sum-total))
                        ans = total
                        # print("<")
                        # print([arr[i],arr[left],arr[right]])
                        # print(score)
                        # print(ans)
                    left += 1
                elif total > target_sum:
                    if score > abs(target_sum-total):
                        score = min(score,abs(target_sum-total))
                        ans = total
                        # print(">")
                        # print([arr[i],arr[left],arr[right]])
                        # print(score)
                        # print(ans)
                    right -= 1
                else:
                    return target_sum

            
        # print("-----------------------------")
        return ans
