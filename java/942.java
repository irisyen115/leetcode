class Solution {
    public int[] diStringMatch(String s) {
        int[] ans = new int[s.length()+1];
        int I = 0, D = ans.length-1;
        for(int i = 0; i < ans.length-1; i++) {
            if(s.charAt(i) == 'I') {
                ans[i] = I++;
            } else {
                ans[i] = D--;
            }
        }    
        ans[ans.length-1] = I;                            
        return ans; 
    }
}
