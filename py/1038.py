class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.acc = 0
        def dfs(node):
            if not node: return                        
            dfs(node.right)
            self.acc = node.val = node.val + self.acc            
            dfs(node.left)
            return node
        return dfs(root)