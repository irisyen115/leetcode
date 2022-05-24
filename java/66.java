class Solution {
    public int[] plusOne(int[] digits) {
        int []nums = new int [digits.length+1];
        int carry = 0;
        nums[0] = 1;
        
        digits[digits.length-1] += 1;
        for (int i = digits.length-1; i >= 0 ; i--){
            digits[i] += carry;
            nums[i+1] = digits[i];
            
            if (digits[i] > 9){
                carry = 1;
                nums[i+1] = 0;
                digits[i] = 0;
            } else {
                carry = 0;
            }
        }
        
        if(carry == 1){
            return nums;
        } else {
            return digits;
        }
    }
}
