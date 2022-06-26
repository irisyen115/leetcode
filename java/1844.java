class Solution {
    public String replaceDigits(String s) {
        char[] ans = s.toCharArray();
        
        for(int i = 1; i < ans.length; i+=2){
            int myInt = ans[i-1] + (ans[i] - '0');
            ans[i] = ((char)myInt);
            
        }
        return String.valueOf(ans);
    }
}
