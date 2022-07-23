class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int total = 0;
        int[] p = new int[arr.length+1];
        p[0] = 0;
        for(int i = 1; i < p.length; i++) {
            p[i] = p[i-1] + arr[i-1];
        }
        for(int x = 1; x < p.length; x+=2) {
            for(int i = 0; i < p.length-x; i++) {
                total += (p[i+x] - p[i]);
            }
        }
        return total;
    }
}
