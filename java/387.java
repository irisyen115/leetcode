class Solution {
    public int firstUniqChar(String s) {
        char[] ans = s.toCharArray();
        int[] letter = new int[26];
        for(int i = 0; i < ans.length; i++) {
            letter[ans[i] -'a'] = letter[ans[i] -'a'] + 1;
        }
        for(int i = 0; i < ans.length; i++) {
            if(letter[ans[i] -'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
