class Solution {
    public boolean halvesAreAlike(String s) {
        String s1 = s.substring(0,(s.length()/2));
        String s2 = s.substring((s.length()/2),(s.length()));
        
        int count1 = 0;
        int count2 = 0;
        for(char ch:s1.toCharArray()) {
            if(ch-'a' < 97) {
                ch = Character.toLowerCase(ch);
            }
            if(ch-'a' == 'a'-'a' || ch-'a' == 'e'-'a' || ch-'a' == 'i'-'a' || ch-'a' == 'o'-'a' || ch-'a' == 'u'-'a') {
                count1++;
            } 
        }
        for(char ch:s2.toCharArray()) {
            if(ch-'a' < 97) {
                ch = Character.toLowerCase(ch);
            }
            if(ch-'a' == 'a'-'a' || ch-'a' == 'e'-'a' || ch-'a' == 'i'-'a' || ch-'a' == 'o'-'a' || ch-'a' == 'u'-'a') {
                count2++;
            } 
        }
        return count1==count2;        
    }
}
