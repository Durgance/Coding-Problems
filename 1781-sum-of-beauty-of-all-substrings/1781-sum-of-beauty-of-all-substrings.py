class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                # print(s[i:j])
                d = Counter(s[i:j])
                # print(d)
                all_count = d.values()
                if len(d.values())==0:
                    continue
                total += max(all_count) - min(all_count)
        return total