from typing import defaultdict
from typing import List
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        if m<1:
            return [-1]
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        queue=[]
        distance=[float('inf')] * (n+1)
        parent= [ i for i in range(n+1)]
        distance[1]=0
        heapq.heappush(queue,(0,1))
        while queue:
            curr_dist,curr_node=heapq.heappop(queue)
            if curr_dist>distance[curr_node]:
                continue
            for neighbor,dist in adj[curr_node]:
                if distance[neighbor]>dist+distance[curr_node]:
                    distance[neighbor]=dist+distance[curr_node]
                    parent[neighbor]=curr_node
                    heapq.heappush(queue,(distance[neighbor],neighbor))
        if distance[n]==float('inf'):
            return [-1]
        path=[]
        ver=n
        path.append(distance[n])
        while parent[ver]!=ver:
            path.append(ver)
            ver=parent[ver]
        path.append(1)
        return path   