class Solution {
    public int majorityElement(int[] nums) {
        int K = nums.length/2;
        TreeMap<Integer,Integer> map = new TreeMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue()>K) return entry.getKey();
}return 1;
    }
}