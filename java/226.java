class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;
        TreeNode tmp = new TreeNode();
        TreeNode leftRoot = invertTree(root.left);
        TreeNode rightRoot = invertTree(root.right);
        
        tmp = leftRoot;
        root.left = rightRoot;
        root.right = tmp;
        
        return root;
    }
}
