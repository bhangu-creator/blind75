from collections import defaultdict
from collections import deque

class Solution:

    #bipartite graph is defined as a graph in which every vertex of graph can be colored in two colors given that no two adjacent vertex have the same color
    #if a graph has a cycle of odd length than that graph can never be bipartite, other than this every graph can be bipartite
    #any question where they give us a hint of dividing the elements in two than in that problem we can use the bipartite graph logic
    def isBipartite(self, V, edges):
        colored=[-1] * V
        adj=defaultdict(list)
        
        for vertex1,vertex2 in edges:
            adj[vertex1].append(vertex2)
        def dfs(vertex,color):
            colored[vertex]=color
            for neighbor in adj[vertex]:
                if colored[neighbor]==-1:
                    newColor=1-color
                    if not dfs(neighbor,newColor):
                        return False
                elif colored[neighbor]==color:
                    return False
            return True
        for vertex in range(V):
            if colored[vertex]==-1:
                if not dfs(vertex,1):
                    return False
        return True

    #using bfs:

    def isBipartite(self, V, edges):
        colored=[-1] * V
        adj=defaultdict(list)
        
        for vertex1,vertex2 in edges:
            adj[vertex1].append(vertex2)
            
        def bfs(vertex,color):
            queue=deque()
            colored[vertex]=color
            queue.append(vertex)
            while queue:
                node=queue.popleft()
                for neighbor in adj[node]:
                    if colored[neighbor]==-1:
                        colored[neighbor]=1-colored[node]
                        queue.append(neighbor)
                    elif colored[neighbor]==colored[node]:
                        return False
            return True
        for vertex in range(V):
            if colored[vertex]==-1:
                if not bfs(vertex,1):
                    return False
        return True
        