class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        start = 0 
        matched = 0
        char_freq = {}
        for char in s1:
            char_freq[char] = 1 + char_freq.get(char,0)
        
        n = len(s2)
        for end in range(n):
            right_char = s2[end]
            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            
            if matched == len(char_freq):return True

            if end - start +1 >= len(s1):
                left_char = s2[start]
                start+=1
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -=1
                    char_freq[left_char] += 1
        
        return False
