class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        start = 0
        flag = False
        for i in range(len(word)):
            if word[i]==ch:
                end = i
                print(end)
                flag = True
                break
        if flag == False :
            return word
        return "".join(reversed(word[:end+1]))+word[end+1:]