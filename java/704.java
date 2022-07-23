class Solution {
    public int search(int[] nums, int target) {
        int left = -1;
        int right = nums.length;
        int middle = 0;
        while(left+1 < right) {
            middle = (left + right) / 2;                
            if(nums[middle] <= target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        if(left >= 0 && target != nums[left]) {
            return -1;
        } else{
            return left;    
        }
    }
}
