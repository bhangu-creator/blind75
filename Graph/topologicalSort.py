from collections import defaultdict
from collections import deque


class Solution:
    

    #this is topologic sort using the dfs approach
    #topologic states that given an edge between u and v , the u vertex will always come before v in the order, and it is always true for every edge in the graph
    #intuation is very simple. we start from first vertex say u, now its neighbors are all the vertex which comes after it so we can say they are all v, so u should come before v in the topo sort. so what we do is we use a stack 
    #to push all the v's first in the stack and in end we push the u itself, we do this with help of recursion, keep on exploring v's until we can't and when we are coming back just keep on storing them in stack that way every u will come ahead of v .
    def topoSort(self, V, edges):
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        visited=[False]* V
        self.stack=[]
        def dfs(node):
            if not visited[node]:
                visited[node]=True
                for neighbor in adj[node]:
                    dfs(neighbor)
                self.stack.append(node)
        for ver in range(V):
            if not visited[ver]:
                dfs(ver)
        return self.stack[::-1]


#using bfs
#this uses the concept of indegree, where indegree represents the number of arrows pointed to a node, we use kahn's algo with this, it states that append all the nodes with degree==0 in queue and then pop them 1 by 1 to apply bfs on them and only apend them when indegree becomes 0 
    def topoSort(self, V, edges):
        adj = defaultdict(list)
        indegree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return topo


sol=Solution()
sol.topoSort(5,[[0,4],[2,4],[1,3],[1,0]])
