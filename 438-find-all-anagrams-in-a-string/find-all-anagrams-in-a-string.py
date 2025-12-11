class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        ans = []
        matched = 0
        freq_map = {}
        for char in p:
            freq_map[char] = 1 + freq_map.get(char,0)
        n = len(s)
        for end in range(n):
            right_char = s[end]
            if right_char in freq_map:
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched += 1
            
            if matched == len(freq_map):
                ans.append(start)
            
            if end - start +1 >= len(p):
                left_char = s[start]
                start+=1
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched -= 1 # removing the matched element form the window and reducing the match count
                    freq_map[left_char] += 1 # adding back the removed element from the window 
        return ans
                