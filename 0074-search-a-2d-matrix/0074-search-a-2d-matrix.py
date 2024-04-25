class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for i in range(row):
            for j in range(col):
                if target == matrix[i][j]:
                    return True
        
        return False