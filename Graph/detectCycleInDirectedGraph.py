from collections import defaultdict

class Solution:

    #we are using a recur visited to maintain track of all the nodes in the current recursion, since it is directed graph we dont have to track the parent we just have to see if we revist the node in the current recursion stack
    def isCycle(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V
        recursion_stack = [False] * V

        def dfs(node):
            visited[node] = True
            recursion_stack[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recursion_stack[neighbor]:
                    return True

            recursion_stack[node] = False
            return False

        for v in range(V):
            if not visited[v]:
                if dfs(v):
                    return True

        return False
