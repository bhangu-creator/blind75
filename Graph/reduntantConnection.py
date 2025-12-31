
from typing import List;
from collections import defaultdict;
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        adj=defaultdict(list)

        def dfs(node,par):
            visited[node]=True
            parent[node]=par
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor,node):
                        return True
                elif neighbor!=parent[node]:
                    return True
            return False

        for indx in range(n):
            visited=[False] * (n+1)
            parent=[False] * (n+1)
            u,v=edges[indx]
            adj[u].append(v)
            adj[v].append(u)
            if dfs(u,-1):
                return edges[indx]
#approch is kind of brute force , it is O(n) square time and O(n) space. 
#we build the graph edge by edge while keep doing dfs each time, the edge that make the graph into cycle we simply return that edge
        