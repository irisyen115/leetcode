class Solution {
    public int[][] flipAndInvertImage(int[][] image) {                
        for(int[] nums:image) {
            int head = 0;
            int tail = nums.length-1;
            int tmp;
            while(head < tail) {
                tmp = nums[head];
                nums[head] = nums[tail];
                nums[tail] = tmp;
                if(nums[head] == 0) {
                    nums[head] = 1;
                } else {
                    nums[head] = 0;
                }
                if(nums[tail] == 0) {
                    nums[tail] = 1;
                } else {
                    nums[tail] = 0;
                }                
                head++;
                tail--;
                }  
            if(nums.length % 2 == 1 && nums[nums.length/2] == 0) {
                nums[nums.length/2] = 1;
            } else if(nums.length % 2 == 1 && nums[nums.length/2] == 1){
                nums[nums.length/2] = 0;
            }
            }    
        return image;
        }
}


