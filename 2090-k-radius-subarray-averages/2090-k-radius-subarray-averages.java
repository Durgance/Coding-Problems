class Solution {
    public int[] getAverages(int[] nums, int k) {
        int[] ans = new int[nums.length];
        // Arrays.fill(ans,-1);
        // int start = 0;
        // int end = k+k;
        
        // Sliding Window Problem
        if (k==0) return nums;
        int pos = k;
        long div = k+k+1;
        long total = 0;
        for(int start=0;start<nums.length;start++){
            
            total += nums[start];
            if (start>=div-1){
                ans[pos] = (int)(total/div);
                total -= nums[start-k-k];
                pos++;
            }if(k!=0){
                ans[start]=-1;
            }
        }
        
        return ans;

    }
}