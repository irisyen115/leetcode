class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        stack = [0]

        def dfs(graph, node, target):
            if node == target:
                ans.append(stack[:])
            else:
                for n in graph[node]:
                    stack.append(n)
                    dfs(graph, n, target)
                    stack.pop()

        dfs(graph, 0, len(graph) - 1)
        return ans