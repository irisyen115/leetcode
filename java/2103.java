class Solution {
    public int countPoints(String rings) {
        char[] chars = rings.toCharArray();
        boolean[][] ans = new boolean[10][3];
        int count = 0;
        
        for(boolean[] row:ans){
            for(boolean j:row){
                j = false;
            }
        }
        
        for(int i = 1; i < chars.length; i+=2){
            int row = chars[i] - '0';
            if(chars[i-1] == 'B'){
                ans[row][0] = true;
            }
            if(chars[i-1] == 'G'){
                ans[row][1] = true;
            } 
            if(chars[i-1] == 'R'){
                ans[row][2] = true;
            }
        }
        for(int i = 0; i < ans.length; i++){
            if(ans[i][0] == true && ans[i][1] == true && ans[i][2] == true){ 
                count++;
            }
        }
        
        return count;
    }
}
