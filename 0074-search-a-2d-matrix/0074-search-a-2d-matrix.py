class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        
        # using BS
        collect = []
        for i in matrix :
            collect.extend(i)
        low = 0
        high = len(collect) - 1
        while low <= high:
            mid = (high+low)//2
            if collect[mid] == target:
                return True
            elif collect[mid] > target:
                high = mid - 1
            elif collect[mid] <target:
                low = mid + 1
        return False
        