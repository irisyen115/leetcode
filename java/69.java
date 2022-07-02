class Solution {
    public int mySqrt(int x) {
        int left = -1;
        int right = 46341;
        while(left + 1 < right){
            int middle = (left+right)/2;
            if(middle * middle <= x) {
                left = middle;
            } else {
                right = middle;
            }
        }
        return left;
    }
}
