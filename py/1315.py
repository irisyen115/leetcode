# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        def dfs(node, parent, grandparent):
            if not node: return
            if grandparent % 2 == 0:
                self.total += node.val
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
            return self.total
        dfs(root, 1, 1)
        return self.total