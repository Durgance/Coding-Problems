class Solution:
    def frequencySort(self, s: str) -> str:
        l =[]
        d = Counter(s)
        for key,val in d.items():
            heappush(l,(-1*val,key))
        # print(l)
        ans = ""
        while len(l)!=0:
            val , key = heappop(l)
            ans += key*(-1*val)
        return ans