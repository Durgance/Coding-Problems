class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        if (matrix[0][0]>target || matrix[row-1][col-1]<target)return false;
        
        for(int i=0;i<row;i++){
            if (matrix[i][col-1]>=target){
                for(int j=0;j<col;j++){
                    if (matrix[i][j]==target) return true;
                }
                break;
            }
        }
        return false;
    }
}