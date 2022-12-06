# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [root]
        while any(node.left is not None or node.right is not None for node in level):
            level = [x for node in level for x in (node.left, node.right) if x is not None]       
        return sum(node.val for node in level)
             