class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left = 0
        right = 0
        temp = ""
        max_count = 0

        while right<len(s):
            temp = s[left:right]
            if len(temp) == 0:
                right += 1
                continue
            if s[right] in temp:
                left += 1 
                right = left
                temp = ""
                continue
            if len(temp)>0:
                max_count = max(max_count,len(s[left:right])) 
            right += 1
        return max_count + 1 