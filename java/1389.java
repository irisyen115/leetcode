class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int[] wer = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            ans.add(index[i],nums[i]);            
        }
        int i = 0;
        for (int val :ans) {
            wer[i++] = val;
        }       
        return wer;
    }
}
