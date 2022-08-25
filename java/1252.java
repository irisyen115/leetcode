class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int count = 0;
        int[][] ans = new int[m][n];
        for(int i = 0; i < indices.length; i++) {            
            for(int row = 0; row < ans[indices[i][0]].length; row++) {
                ans[indices[i][0]][row] += 1;
            }
            for(int col = 0; col < ans.length; col++) {
                ans[col][indices[i][1]] += 1;
            }
        }
        
        for(int[] row:ans) {
            for(int num:row) {
                if(num % 2 == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}