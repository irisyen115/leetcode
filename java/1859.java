class Solution {
    public String sortSentence(String s) {
        String []a = s.split(" ");
        String []ans = new String[a.length];
        
        for(String st:a){
            int lastInt = st.charAt(st.length() - 1) - '0';
            ans[lastInt-1] = st.substring(0, st.length() - 1);
        }
        
        return String.join(" " ,ans);
    }
}
