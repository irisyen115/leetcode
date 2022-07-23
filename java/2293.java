class Solution {
    public int minMaxGame(int[] nums) {
        int num = 0;
        while(nums.length > 2) {
          int[] newArray  = new int[nums.length / 2];
          for(int i = 0; i < nums.length/2; i+=2) {
              newArray[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
              newArray[i + 1] = Math.max(nums[2 * (i+1)], nums[2 * (i+1) + 1]);
          }
          nums = newArray;
        }
        if (nums.length == 1) {
            num = nums[0];
        } else{
            num = Math.min(nums[0],nums[1]);
        }
        
        
        return num;
    }
}
