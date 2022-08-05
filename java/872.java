class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> ans1 = getlist(root1);
        List<Integer> ans2 = getlist(root2);
        
        if(ans1.size() != ans2.size()) return false;
        for(int i = 0; i < ans1.size(); i++) {
            if(ans1.get(i) != ans2.get(i)) {
                return false;
            } 
        }
        return true;
    }
    
    public List<Integer> getlist(TreeNode root){
        List<Integer> ans = new ArrayList<Integer>();
        if(root == null) return ans;        
        if(root.left == null && root.right == null) {
            ans.add(root.val);
            return ans;
        }
        
        ans.addAll(getlist(root.left));
        ans.addAll(getlist(root.right));
        
        return ans;
    }
}
