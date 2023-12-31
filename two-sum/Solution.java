class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nums_map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int comp = target - nums[i];
            if(nums_map.containsKey(comp)){
                return new int[] {nums_map.get(comp), i};
            }
            nums_map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No match Found");
    }
}
