class Solution {
    public TreeNode increasingBST(TreeNode root) {
        if(root == null) return null;
                
        TreeNode up = increasingBST(root.left);
        TreeNode down = increasingBST(root.right);
        TreeNode cur = up;
        root.left = null;
        
        if(up == null){            
            root.right = down;
            return root;
        } 
        
        while(cur.right != null) {
            cur = cur.right;
        }
        
        cur.right = root;
        root.right = down;
        return up;        
    }
}
