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
                head++;
                tail--;
            }
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] == 0) {
                    nums[i] = 1;
                } else {
                    nums[i] = 0;
                }
            }                        
        }
        return image;
    }
}
    

