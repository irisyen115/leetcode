class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 1;
        
        for(int i = 0; i < sentences.length; i++) {
            String []ans = sentences[i].split(" ");
            if(max < ans.length){
                max = ans.length;
            }
            // max = Math.max(max,st.split(" ").length);
        }
        return max;
    }
}
