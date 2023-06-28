# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root])
        count = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    if cur.left.left == None and cur.left.right == None:
                        count += cur.left.val                    
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return count