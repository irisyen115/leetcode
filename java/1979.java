class Solution {
    public int findGCD(int[] nums) {
        int M = 0, m = 1001;
        for(int i :nums){
            if(i > M){
                M = i;
            } 
            if(i < m){
                m = i;
            }
        }
        return gcd(m,M);
    }
    private int gcd(int a,int b) {
        if(a % b == 0){
            return b;
        } else {
            return gcd(b, a % b);
        }
    }
}
