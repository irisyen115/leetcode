# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            if root == None:
                return []
            else:
                return inorder(root.left) + [root.val] + inorder(root.right)

        nums = inorder(root)
        
        m = float('inf')
        for a,b in zip(nums, nums[1:]):
            m = min(m, abs(a - b))

        return m