class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        int left = 0;
        int right = mat.length-1;
        
        for (int row = 0; row < mat.length; row++, right--,left++){
            sum += mat[row][left];
            if (left != right){
                sum += mat[row][right];
            }
            
        }
        // for (int []row : mat) {
        //     sum+=row[left];
        //     if (left != right) {
        //         sum += row[right];
        //     }
        //     left++;
        //     right--;
        // }
        return sum;
    }
}
