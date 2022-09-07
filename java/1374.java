class Solution {
    public String generateTheString(int n) {
        String ans = "";
        for(int i = 0; i < n-1; i++) {            
            ans += 'a';
        }
        if(n % 2 == 0) {
            ans += 'b';
        } else {
            ans += 'a';
        }
        return ans;
    }
}