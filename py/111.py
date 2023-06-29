# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def level(node):
            if not node:
                return 0
            if node.left and node.right:
                return min(level(node.left), level(node.right)) + 1
            if node.left is None:
                return level(node.right) + 1
            elif node.right is None:
                return level(node.left) + 1
        return level(root)