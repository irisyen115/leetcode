class Solution {
    public boolean squareIsWhite(String coordinates) {
        char[] ans = coordinates.toCharArray();
        if((ans[0] - 'a') % 2 == 0) {
            if(ans[1] % 2 == 0) {
                return true;
            } 
        } else {
            if(ans[1] % 2 == 1) {
                return true;
            }
        }
        return false;        
    }
}