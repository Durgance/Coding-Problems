class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start , max_len = 0, 0
        char_freq = {}
        for end,char in enumerate(fruits):
            right_char = char
            char_freq[right_char] = 1 + char_freq.get(right_char,0)

            while len(char_freq)>2:
                # print(fruits[start:end+1])
                left_char = fruits[start]
                char_freq[left_char] -= 1
                if char_freq[left_char] <1:
                    del char_freq[left_char]
                start += 1
            max_len = max(max_len,end-start+1)
        return max_len 