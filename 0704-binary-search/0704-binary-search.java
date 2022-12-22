class Solution {
    public int search(int[] nums, int target) {
        // Arrays.sort(nums);
        int ans= Arrays.binarySearch(nums,target);
        if (ans<0) return -1;
        return ans;
    }
}