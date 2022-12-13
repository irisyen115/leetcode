# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(roota, rootb):
            if not roota and not rootb:
                return True
            elif not roota or not rootb:
                return False
            elif roota.val != rootb.val:
                return False
            return dfs(roota.left, rootb.left) and dfs(roota.right, rootb.right) 
        return dfs(p, q)       