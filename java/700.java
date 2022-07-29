class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null) return null;
        else {
            if(root.val > val) {
                TreeNode leftNode = searchBST(root.left, val);
                return leftNode;
            } else if(root.val < val) {
                TreeNode rightNode = searchBST(root.right, val);
                return rightNode;
            }
        }
        return root;
    }
}
