class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE,curr,currMax=0,max=0;
        for(int price :prices){
            curr = price;
            min = Math.min(curr,min);
            max = Math.max(curr-min,max); 
        }
        return max;
        
        
        
    }
}