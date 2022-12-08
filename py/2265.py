# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node):
    if not node:
        return 0,0,0        
    sum_l, count_l, ans_l = dfs(node.left)
    sum_r, count_r, ans_r = dfs(node.right)
    if (sum_l + sum_r + node.val) // (count_l + count_r + 1) == node.val:
        return (sum_l + sum_r + node.val) , (count_l + count_r + 1), (ans_l + ans_r + 1)
    else:
        return (sum_l + sum_r + node.val) , (count_l + count_r + 1), (ans_l + ans_r)
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return dfs(root)[2]