class Solution {
    public int[] rearrangeArray(int[] nums) {
        int N = nums.length;
        int[] even = new int[N/2];
        int[] odd = new int[N/2];
        int i=0,j=0;
        for(int num: nums){
            if(num>=0) even[i++] = num;
            else odd[j++] = num;
        }
        
        for(int k=0;k<N;k+=2){
            nums[k] = even[k/2];
            nums[k+1] = odd[k/2];
        }
        return nums;

    }
}