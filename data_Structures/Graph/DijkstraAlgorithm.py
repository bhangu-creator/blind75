from collections import defaultdict
import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        queue=[]
        distance=[float('inf')] * V
        distance[src]=0
        heapq.heappush(queue,(0,src))
        while queue:
            curr_dist,curr_node=heapq.heappop(queue)
            if curr_dist>distance[curr_node]:
                continue
            for neighbor,dist in adj[curr_node]:
                if distance[neighbor]>dist+distance[curr_node]:
                    distance[neighbor]=dist+distance[curr_node]
                    heapq.heappush(queue,(distance[neighbor],neighbor))
        return distance
                
                
                
        