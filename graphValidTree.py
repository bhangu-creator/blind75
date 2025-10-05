from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1:
            return False
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited=[False] * n

        def dfs(node,parent):
            visited[node]=True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor,node):
                        return False
                elif parent!=neighbor:
                    return False
            return True
        return dfs(0,-1)
#the intiuation is to remember that to make graph a valid tree two things are needed , the no of edges must not be less than n-1 , means if there are n nodes then edges must not be less than n-1
#the second condition is that there must not be any cycle in the graph.
#also if the graph is disconneced the edges will be small then n-1 and there for return False
#so we just checked these two conditions above and if they pass we returned True
#time is O(V+E) and space is also O(V+E) due to adj list



            