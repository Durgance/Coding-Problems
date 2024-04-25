class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while True :
            temp = s
            for i in range(len(temp)):
                if temp[i:len(part)+i] == part:
                    s = s[:i] + s[len(part)+i:]
                    break
            if len(temp) == len(s):
                break
        return s