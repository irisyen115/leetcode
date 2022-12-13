# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """     
        if not preorder:
            return None  
        root = TreeNode(preorder[0])        
        left = [v for v in preorder if v < root.val] 
        right = [v for v in preorder if v > root.val]          
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root
            