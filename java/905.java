class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int head = 0;
        int tail = nums.length-1;
        while(head < tail) {
            int tmp;
            while (nums[head] % 2 == 0 && head < nums.length-1) {
                head++;
            }
            while (nums[tail] % 2 == 1 && tail > 0) {
                tail--;
            }
            if(head < tail) {
                tmp = nums[head];
                nums[head] = nums[tail];
                nums[tail] = tmp;
            } else {
                break;
            }
        }
        return nums;
    }
}
