class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len , max_char_len ,start = 0,0,0
        char_freq = {}
        n = len(s)
        for end in range(n):
            right_char = s[end]
            char_freq[right_char] = 1 + char_freq.get(right_char,0)

            # get me the max number of repeated char in the window
            max_char_len = max(max_char_len,char_freq[right_char])
            # more the strat of the window when the number of character 
            # needed to change exceed the limit of char that can be changed 
            # here we can change a max of k char . so we are taking 
            # len of window - length of the repeated char which should be less then 
            # number of char to replace then we move the window by 1
            while (end - start +1 - max_char_len)>k:
                left_char = s[start]
                char_freq[left_char]-=1
                start+=1
            # get me the max value of the window which follows these conditions
            max_len = max(max_len, end - start +1)
        return max_len