class Solution {
    public String restoreString(String s, int[] indices) {
        char []ans = new char[indices.length];
        char []c = s.toCharArray();
        String ansr = "";
        for(int i = 0; i < indices.length; i++){
            ans[indices[i]] = c[i];            
        }
        for(char ch:ans){
            ansr += ch; 
        }
        return ansr;
    }
}
