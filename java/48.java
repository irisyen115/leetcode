class Solution {
    public void rotate(int[][] matrix) {
        int head = 0;
        int tail = matrix.length - 1;

        while (head < tail) {
            int[] tmp;
            tmp = matrix[head];
            matrix[head] = matrix[tail];
            matrix[tail] = tmp;
            head++;
            tail--;
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = i + 1; j < matrix.length; j++) {
                int tmp;
                tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }
}