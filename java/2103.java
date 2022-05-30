class Solution {
    public int countPoints(String rings) {
        char[] chars = rings.toCharArray();
        int[][] ans = new int[10][3];
        int count = 0;
        
        for(int i = 1; i < chars.length; i+=2){
            int row = chars[i] - '0';
            if(chars[i-1] == 'B'){
                ans[row][0] += 1;
            }
            if(chars[i-1] == 'G'){
                ans[row][1] += 1;
            } 
            if(chars[i-1] == 'R'){
                ans[row][2] += 1;
            }
        }
        for(int i = 0; i < ans.length; i++){
            if(ans[i][0] > 0 && ans[i][1] > 0 && ans[i][2] > 0){ 
                count++;
            }
        }
        
        return count;
    }
}
