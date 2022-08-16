class Solution {
    public int[] sortArrayByParity(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            int tmp;
            if(nums.length <= 1) break;
            for(int j = i+1; j < nums.length; j++) {
                if(nums[j] % 2 == 0) {
                    tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                }
            }
        }
        return nums;
    }
}
