class Solution {
    public int subtractProductAndSum(int n) {
        int[] ans = new int[5];
        int mult = 1;
        int sum = 0;
        while(n != 0) {            
            mult *= n%10;
            sum += n%10;
            n /= 10;
        }
        return mult - sum;
    }
}
