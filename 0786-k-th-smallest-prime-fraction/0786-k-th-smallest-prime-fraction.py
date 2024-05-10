class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)
        d = {}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                heappush(heap,arr[i]/arr[j])
                d[arr[i]/arr[j]] = [arr[i],arr[j]]
        
        while 0<=k:
            if k==1:
                return d[heappop(heap)]
            heappop(heap)
            k-=1
         