from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node):
    if not node:
        return 0,0        
    sum_l, count_l = dfs(node.left)
    sum_r, count_r = dfs(node.right)
    return (sum_l + sum_r + node.val) , (count_l + count_r + 1)
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append(root)
        ans = 0
        while q:
            node = q.popleft()
            c, n = dfs(node)
            if c // n == node.val:
                ans += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans