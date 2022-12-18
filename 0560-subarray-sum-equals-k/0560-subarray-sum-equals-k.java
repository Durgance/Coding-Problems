class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int currSum = 0;
        int count= 0;
        for(int num :nums){
            currSum += num;

            if (currSum==k)count++;

            count += map.getOrDefault(currSum-k,0);

            map.put(currSum,map.getOrDefault(currSum,0)+1);
             
        }
        return count;
    }
}