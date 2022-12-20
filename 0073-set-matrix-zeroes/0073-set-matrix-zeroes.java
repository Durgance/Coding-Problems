class Solution {
    public void setZeroes(int[][] matrix) {
        HashSet<Integer> rows = new HashSet<>();
        HashSet<Integer> cols = new HashSet<>();
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if (matrix[i][j]==0){
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        
        // Giving zero to rows
        for(int row:rows){
            for(int i=0;i<matrix[0].length;i++){
                matrix[row][i] = 0;
            }
        }

        //Giving Zero to columns
        for(int col:cols){
            for(int i=0;i<matrix.length;i++){
                matrix[i][col]=0;
            }
        }

    }
}