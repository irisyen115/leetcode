class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[] dict = new int[26];
        int count = 0;
        
        for(char ch:s.toCharArray()) {
            count = dict[ch-'a'] = dict[ch - 'a'] + 1;
        }
        
        for(int in:dict){
            if(in != count && in != 0) {
                return false;
            } 
        }
        return true;
    }
}
