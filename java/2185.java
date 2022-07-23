class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for(String st:words) {
            if(st.length() < pref.length()) {
                continue;
            } 
            String b = st.substring(0,pref.length());                        
            if(b.equals(pref)) {
                count++;
            }
        }
        return count;
    }
}
