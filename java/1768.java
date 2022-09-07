class Solution {
    public String mergeAlternately(String word1, String word2) {
        int st_short_len = Math.min(word1.length(),  word2.length());
        String ans = "";
        for(int i = 0; i < st_short_len; i++) {
            ans += word1.charAt(i);
            ans += word2.charAt(i);
        }
        return ans + word1.substring(st_short_len) + word2.substring(st_short_len);
    }
}