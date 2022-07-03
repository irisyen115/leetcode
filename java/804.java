class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        HashSet<String> s = new HashSet<String>();
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        for(String st:words) {
            String ans = "";
            char[] b = st.toCharArray();
            for (char ch:b) {
                ans += morse[ch-'a'];
            }
            s.add(ans);
        }       
        
        return s.size();
        
    }
}
