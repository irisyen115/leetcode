from collections import deque

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
        def bfs(root):
            ans = []    
            q = deque()            
            q.append(root)
            while q:            
                x = q.popleft()
                if x is None:
                    break
                ans.append(x.val)            
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right) 
            return ans
        return sorted(bfs(root1) + bfs(root2))
        