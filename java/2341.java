class Solution {
    public int[] numberOfPairs(int[] nums) {
        int[] ans = new int[2];
        int[] boxes = new int[101];
        for(int i = 0; i < nums.length; i++) {
            boxes[nums[i]] += 1;
        }
        for(int box:boxes) {                        
            ans[0] += box / 2;
            ans[1] += box % 2;            
        }
        return ans;
    }
}