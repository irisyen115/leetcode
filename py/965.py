from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root) 
        while q:            
            x = q.popleft()
            if x.val != root.val:
                return False
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)          
        return True