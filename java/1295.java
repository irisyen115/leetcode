class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int num: nums) {
            if(digits(num) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
    private int digits(int num) {
        return num < 10 ? 1 : num < 100 ? 2 : num < 1000 ? 3:
               num < 10000 ? 4: num < 100000 ? 5: 6;
    }
}