class Solution:
    def binarySearch(self,arr,target):
        print(arr)
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low + ((high-low)//2)
            if arr[mid] == target:
                return True
            elif arr[mid] > target :
                high = mid - 1
            elif arr[mid] < target :
                low = mid + 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        for i in range(row):
            if matrix[i][0] <= target and matrix[i][-1] >= target :
                if self.binarySearch(matrix[i],target):
                    return True
        
        return False