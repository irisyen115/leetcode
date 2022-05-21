class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> A = new ArrayList<Integer>();
        int carry = 0;
        
        for(int i = num.length-1; i >= 0; i--){
            int a = num[i] + k % 10 + carry;
            carry = a/10;
            A.add(a % 10);
            k = k/10;
        }
        while(k != 0){
            int a = k % 10 + carry;
            carry = a/10;
            A.add(a % 10);
            k = k/10;
        }
        if (carry != 0){
            A.add(carry);
        }
        Collections.reverse(A);
        return A;
    }
}
