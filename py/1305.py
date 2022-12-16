# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """        
        def inorder(root):
            return [] if root is None else inorder(root.left) + [root.val] + inorder(root.right)

        ans = []
        a = inorder(root1)
        b = inorder(root2)
        ai = 0
        bi = 0
        while ai < len(a) and bi < len(b):
            if a[ai] <= b[bi]:
                ans.append(a[ai])
                ai += 1
            else:
                ans.append(b[bi])
                bi += 1
        if  ai < len(a):
            ans.extend(a[ai:])
        elif bi < len(b):
            ans.extend(b[bi:])
        return ans
        