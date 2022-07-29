class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {      
        int sum = 0;
        if(root == null) return 0;        
        
        if(root.val < low) {
            sum += rangeSumBST(root.right, low, high);
        } else if(root.val > high) {
            sum += rangeSumBST(root.left, low, high);
        } else {
            sum += rangeSumBST(root.right, low, high) + rangeSumBST(root.left, low, high); 
        }
        if(root.val >= low && root.val <= high) {
            sum += root.val;
        }
        
        return sum;
    }
}
