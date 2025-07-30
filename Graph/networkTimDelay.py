from typing import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        distance=[float('inf')] * (n+1)
        distance[0]=distance[k]=0
        queue=[]
        heapq.heappush(queue,[0,k])
        while queue:
            curr_dist,curr_node=heapq.heappop(queue)
            if curr_dist>distance[curr_node]:
                continue
            for neighbor,dist in adj[curr_node]:
                if distance[neighbor]>dist+distance[curr_node]:
                    distance[neighbor]=dist+distance[curr_node]
                    heapq.heappush(queue,[dist+distance[curr_node],neighbor])
        if float('inf') in distance:
            return -1
        else:
            return max(distance)
 
        