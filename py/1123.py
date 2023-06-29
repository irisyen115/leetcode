# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def level(node):
            if not node:
                return 0
            return max(level(node.left), level(node.right)) + 1

        def dfs(node):
            if not node:
                return None
            left, right = level(node.left), level(node.right)
            if left == right:
                return node
            if left > right:
                return dfs(node.left)
            if left < right:
                return dfs(node.right)

        return dfs(root)