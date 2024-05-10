class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(heap,matrix[i][j])
        
        while 0<=k:
            if k==1:
                return heappop(heap)
            heappop(heap)
            k-=1
        return 1
