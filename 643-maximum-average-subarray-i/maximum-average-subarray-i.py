class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        max_sum , start , end = float('-inf'), 0 , k
        win_sum = sum(arr[:k])
        max_sum = max(max_sum,win_sum)
        while end<len(arr):
            
            # print(max_sum,win_sum,arr[start:end])
            win_sum += arr[end] - arr[start]
            max_sum = max(max_sum,win_sum)
            # max_avg = max(max_avg,win_sum/k)
            start += 1
            end += 1
        # print(max_sum , win_sum,arr[start:end])
        return max_sum/k