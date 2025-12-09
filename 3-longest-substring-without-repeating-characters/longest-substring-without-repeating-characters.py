class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start , end = 0,0
        max_len = 0
        char_freq = dict()
        for end in range(n):
            right_char = s[end]
            # if right_char not in char_freq:
            #     char_freq[right_char] = 0
            char_freq[right_char] = 1 + char_freq.get(right_char,0)

            while char_freq[right_char]>1:
                left_char = s[start]
                char_freq[left_char] -= 1
                # if char_freq[left_char]>1:
                #     del char_freq[left_char]
                start+=1
            max_len = max(max_len,end-start+1)
        return max_len