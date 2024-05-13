class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        total_len = 0
        max_len = 0
        max_pal = ""
        while left<=len(s):
            while right<=len(s):
                if s[left:right] == s[left:right][::-1]:
                    total_len = right - left
                    if max_len < total_len:
                        max_len = total_len
                        max_pal = s[left:right]
                right += 1
            if len(max_pal) > len(s[left:]):
                break
            left += 1
            right = left
        return max_pal
