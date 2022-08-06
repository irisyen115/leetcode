class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<TreeNode> prelist = new ArrayList<TreeNode>();
        prelist.add(root);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(root == null) return ans;
        
        while(prelist.size() > 0) {
            List<TreeNode> nextlist = new ArrayList<TreeNode>();        
            List<Integer> innerAl = new ArrayList<Integer>();
            for(TreeNode tn:prelist) {
                innerAl.add(tn.val);
                if(tn.left != null) {
                    nextlist.add(tn.left);
                }
                if(tn.right != null) {
                    nextlist.add(tn.right);
                }
            }
            ans.add(innerAl);
            prelist = nextlist;
        }
        return ans;        
    }
}
