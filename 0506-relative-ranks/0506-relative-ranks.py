class Solution:
    
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        from heapq import heappop, heappush, heapify
        temp = score
        ans = [0]*len(score)
        d = {1:"Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        temp = list(map(lambda x: -1*x,temp))
        heapify(temp)
        # heappop(temp)
        # print(len(temp))
        count = 1
        while True:
            if len(temp) == 0:
                break
            target = -1*heappop(temp)
            for i in range(len(score)):
                if score[i] == target:
                    if d.get(count):
                        ans[i] = d[count]
                        count += 1
                        break
                    else:
                        ans[i] = f"{count}"
                        count+=1
                        break
        return ans