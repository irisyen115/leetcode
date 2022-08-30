class Solution {
    public boolean squareIsWhite(String coordinates) {
        boolean[] squ = new boolean[64];
        char[] ans = coordinates.toCharArray();
        for(int i = 0; i < 64; i++) {
            if((i/8) % 2 == 0 && i % 2 == 1) {
                squ[i] = true;
            }
            if((i/8) % 2 == 1 && i % 2 == 0) {
                squ[i] = true;
            }
        }
        return squ[(int)((ans[0] - 'a') * 8 ) + (((int)(ans[1])-'0') - 1)];        
    }
}