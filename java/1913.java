class Solution {
    public int maxProductDifference(int[] nums) {
        int max1 = -1;
        int max2 = -1;
        int min1 = 100000;
        int min2 = 100000;
        for(int num:nums) {
            if(num > max2) {
                max2 = num;
            }
            if(num > max1) {
                if(num < max2) continue;
                max2 = max1;
                max1 = num;                
            }
            if(num < min2) {
                min2 = num;
            }
            if(num < min1) {
                if(num > min2) continue;
                min2 = min1;
                min1 = num;                
            }
        }        
        return (max1 * max2) - (min1 * min2);
    }
}
