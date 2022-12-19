class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num : nums){
            set.add(num);
        }

        int longestSequence = 0;
        for(int num:nums){
            if (!set.contains(num-1)){
                int currValue = num;
                int currLength = 1;
                while(set.contains(currValue+1)){
                    currValue+=1;
                    currLength +=1;
                }
                longestSequence = Math.max(longestSequence,currLength);
            }
        }
        return longestSequence;
    }
}