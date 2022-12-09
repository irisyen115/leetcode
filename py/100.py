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
        def getlist(root):
            ans = []
            if root is None:
                return ans

            if root.left:
                ans.extend(getlist(root.left))
            else:
                ans.append('null')
            if root.right:
                ans.extend(getlist(root.right))
            else:
                ans.append('null')
            ans.append(root.val)

            return ans
        pl = getlist(p)
        ql = getlist(q)

        return pl == ql
