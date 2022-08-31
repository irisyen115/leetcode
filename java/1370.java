class Solution {
    public String sortString(String s) {
        char[] a = s.toCharArray();
        String ans = "";
        int[] dict = new int[26];        
        for(char ch:a) {
            dict[ch - 'a'] += 1;
        }
        
        while(ans.length() != s.length()) {
            for(int i = 0; i < dict.length; i++) {
                if(dict[i] != 0) {
                    ans += (char)(i + 'a');
                    dict[i]--;
                }
            }
            for(int i = dict.length-1; i > -1; i--) {
                if(dict[i] != 0) {
                    ans += (char)(i + 'a');
                    dict[i]--;
                }  
            }
        }
        return ans;
    }
}