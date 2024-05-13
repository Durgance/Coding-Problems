class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            ans = int("".join(reversed(str(x))))
        else:
            ans = int("".join(reversed(str(x)[1:]))) * -1
        if pow(-2,31) <= ans and ans <= pow(2,31)-1:
            return ans
        return 0