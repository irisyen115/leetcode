class Solution {
    public int[] decompressRLElist(int[] nums) {
        int count = 0;
        for(int i = 0; i < nums.length; i+=2) {
            count += nums[i];
        }
        int[] ans = new int[count];
        List<Integer> s = new ArrayList<>();
        
        for(int i = 0; i < nums.length; i+=2) {
            for(int j = 0; j < nums[i]; j++) {
                s.add(nums[i+1]);
            }
        }
        for(int i = 0; i < s.size(); i++) {
            ans[i] = s.get(i);
        }
        return ans;
    }
}
