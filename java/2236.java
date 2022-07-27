class Solution {
    public boolean checkTree(TreeNode root) {
        boolean add = false;
        (root.left.val + root.right.val == root.val): add = true;
        return add;
    }
