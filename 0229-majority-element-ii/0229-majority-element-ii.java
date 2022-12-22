class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        List<Integer> ans = new ArrayList<>();
        
        for(HashMap.Entry<Integer, Integer> entry : map.entrySet()) {
	        // System.out.println(entry.getKey() + " = " + entry.getValue());
            if (entry.getValue()>nums.length/3){
                ans.add(entry.getKey());
            }
        }
        return ans;           
    }
}