class Solution {
    
    public static void swap(int[] a, int i, int j){
	int temp = a[i];
  	a[i] = a[j];
  	a[j] = temp;
}
    public void reverse(int[] nums,int start,int end){
        while(start<end){
            swap(nums,start,end);
            start++;
            end--;
        }
    }

    public void nextPermutation(int[] nums) {
        // Optimal Approch for Permutation
        int i = nums.length-2;
        while(i>=0 && nums[i]>=nums[i+1]){
            i--;
        }
        if(i>=0){
            int j= nums.length-1;
            while(nums[j]<=nums[i]){
                j--;
            }
            swap(nums,i,j);
        }
        reverse(nums,i+1,nums.length-1);

    }
}