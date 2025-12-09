class Solution:
    def at_most(self,arr,k):
        start , max_len = 0, 0 
        freq_map = {}
        n = len(arr)

        for end in range(n):
            right_win = arr[end]
            freq_map[right_win] = 1 + freq_map.get(right_win,0)

            while len(freq_map)>k:
                left_win = arr[start]
                freq_map[left_win] -= 1
                if freq_map[left_win] < 1:
                    del freq_map[left_win]
                start+=1
            max_len += end - start +1
        return max_len

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums,k) - self.at_most(nums,k-1)