class Solution {
    public int minOperations(int[] nums) {
        int count = 0;
        int index = 0;
        while(index < nums.length-1) {
            if(nums[index+1] > nums[index]) {
                index++;
            } else {
                count += (nums[index] + 1) - nums[index+1];
                nums[index+1] = nums[index] + 1;
                index++;
            }            
        }
        return count;
    }
}