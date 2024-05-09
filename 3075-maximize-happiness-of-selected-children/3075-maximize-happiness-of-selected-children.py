class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        count = 0
        idx = len(happiness) -1
        total_happy = 0
        while k:
            if happiness[idx] - count >= 0:
                total_happy += happiness[idx] -count
            else:
                break
            k -= 1
            count += 1
            idx -= 1
        return total_happy
