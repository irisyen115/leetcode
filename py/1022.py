from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        q.append((root,root.val))
        count = 0
        while q:
            node, val = q.popleft()         
            if node.left:
                q.append((node.left, 2 * val + node.left.val))
            if node.right:
                q.append((node.right, 2 * val + node.right.val))
            if node.left is None and node.right is None:
                count += val
        return count
        
