class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        max_sum , start , end = float('-inf'), 0,0
        win_sum = 0
        while end<len(arr):
            win_sum += arr[end]
            # max_avg = max(max_avg,win_sum/k)
            if end>=k-1:
                max_sum = max(max_sum,win_sum)
                win_sum -= arr[start]
                start += 1
            
            end += 1
        return max_sum/k