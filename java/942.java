class Solution {
    public int[] diStringMatch(String s) {
        int[] ans = new int[s.length()+1];
        char[] a = s.toCharArray();
        int I = 0;
        int D = a.length;
        for(int i = 0; i < a.length; i++) {
            if(a[i] == 'I') {
                ans[i] = I;
                I++;
            } else {
                ans[i] = D;
                D--;
            }
        }
        if(a[a.length-1] == 'I') {
                ans[ans.length-1] = I;                
            } else {
                ans[ans.length-1] = D;                
            }
        return ans; 
    }
}
