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
        level = [root]
        count = 0
        while level:
            next_level = []
            next_next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)                
            for node in level:               
                    if node.val % 2 == 0:                                                       
                        if node.left in next_level:
                            if node.left.left:
                                next_next_level.append(node.left.left)
                            if node.left.right:
                                next_next_level.append(node.left.right)
                        if node.right in next_level:
                            if node.right.left:
                                next_next_level.append(node.right.left)
                            if node.right.right:
                                next_next_level.append(node.right.right)                  
            count += sum(node.val for node in next_next_level)          
            level = next_level
        return count
