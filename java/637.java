class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<TreeNode> prelist = new ArrayList<TreeNode>();
        prelist.add(root);
        List<Double> ans = new ArrayList<Double>();        
        
        while(prelist.size() > 0) {
            List<TreeNode> nextlist = new ArrayList<TreeNode>();
            double sum = 0;                
            for(TreeNode tn:prelist) {
                if(tn.left != null) {
                    nextlist.add(tn.left);                
                }        
                if(tn.right != null) {
                    nextlist.add(tn.right);
                }   
                sum += (double)(tn.val);                
            }
            ans.add(sum/(prelist.size()));
            prelist = nextlist;
        }
        return ans;
    }
}
