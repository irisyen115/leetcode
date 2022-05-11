class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int numbers = ((1+n)*n)/2;
        for (int j = 0; j < n; j++) {
            numbers -= nums[j];
        }
        return numbers;
    }
}
    
class Solution {
    public int missingNumber(int[] nums) {
        int number,j;
        for (number = 0; number < nums.length+1; number++){
            boolean found = false;
            for (j = 0; j < nums.length; j++){
                if (number == nums[j]) {
                    found = true;
                    break;
                }
            }
            if (found == false) {
                return number;
            }
        }
        return number;
    }
}
