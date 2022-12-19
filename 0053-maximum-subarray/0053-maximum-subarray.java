class Solution {
    public int maxSubArray(int[] nums) {
        // Kadane's Algorithm
        int msf = Integer.MIN_VALUE;
        int meh = 0,s=0;
        int start,end;
        for(int i=0;i<nums.length;i++){
            meh += nums[i];
            if(meh>msf){
                msf = meh;
                start =s;
                end = i;
            } 
            if (meh<0){
                meh = 0;
                s = i+1;
            }
        }
        return msf;
    }
}