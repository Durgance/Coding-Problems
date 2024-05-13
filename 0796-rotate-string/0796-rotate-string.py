class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        if Counter(s)!=Counter(goal):
            return False
        for i in range(len(s)):
            if s[i:] + s[:i]  == goal:
                return True
        return False
