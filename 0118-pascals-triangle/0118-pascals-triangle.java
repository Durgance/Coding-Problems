class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        for(int i=0;i<numRows;i++){
            List<Integer> inter = new ArrayList<Integer>();
            for(int j=0;j<i+1;j++){
                if (j==0 || i==j){
                    inter.add(1);
                }else{
                    inter.add(ans.get(i-1).get(j-1)+ans.get(i-1).get(j));
                }
            }
            ans.add(inter);
        }
        return ans;
    }
}