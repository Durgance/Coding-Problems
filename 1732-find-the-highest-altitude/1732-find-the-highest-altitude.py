class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        current = 0
        highest = 0
        prev=0
        for gain in gains:
            current = prev + gain
            prev = current
            highest = max(highest,current)
        return highest