class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {    
        int sum = 0;         
        if(root == null) sum = 0;
        else {
            int leftVal = rangeSumBST(root.left, low, high);
            int rightVal = rangeSumBST(root.right, low, high);
            sum += (leftVal+rightVal);
            if(root.val >= low && root.val <= high) {
                sum += root.val;
            }
        }
        return sum;
    }
}
