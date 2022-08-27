class Solution {
    public int sumOfUnique(int[] nums) {
        int[] record = new int[101];
        int count = 0;
        for(int num:nums) {
            record[num] += 1;
        }
        for(int i = 0; i < record.length; i++) {
            if(record[i] == 1) {
                count += i;
            }
        }
        return count;
    }
}